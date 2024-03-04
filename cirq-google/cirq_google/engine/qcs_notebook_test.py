# Copyright 2021 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import unittest
import unittest.mock as mock
import pytest

import cirq_google as cg
from cirq_google.engine.qcs_notebook import (
    get_qcs_objects_for_notebook,
    QCSObjectsForNotebook,
    get_hardware_engine_and_authenticate_user,
)
from cirq_google.engine.abstract_engine import AbstractEngine


def _assert_correct_types(result: QCSObjectsForNotebook):
    assert isinstance(result.device, cg.GridDevice)
    assert isinstance(result.sampler, cg.ProcessorSampler)
    assert isinstance(result.engine, cg.engine.AbstractEngine)
    assert isinstance(result.processor, cg.engine.AbstractProcessor)


def _assert_simulated_values(result: QCSObjectsForNotebook):
    assert not result.signed_in
    assert result.is_simulator
    assert result.project_id == 'fake_project'


def test_get_qcs_objects_for_notebook_virtual():
    result = get_qcs_objects_for_notebook(virtual=True)
    _assert_correct_types(result)
    _assert_simulated_values(result)
    assert result.processor_id == 'rainbow'
    assert len(result.device.metadata.qubit_set) == 23

    result = get_qcs_objects_for_notebook(processor_id='weber', virtual=True)
    _assert_correct_types(result)
    _assert_simulated_values(result)
    assert result.processor_id == 'weber'
    assert len(result.device.metadata.qubit_set) == 53


@mock.patch('cirq_google.engine.qcs_notebook.get_engine')
def test_get_qcs_objects_for_notebook_mocked_engine_fails(engine_mock):
    """Tests creating an engine object which fails."""
    engine_mock.side_effect = EnvironmentError('This is a mock, not real credentials.')
    result = get_qcs_objects_for_notebook()
    _assert_correct_types(result)
    _assert_simulated_values(result)


@mock.patch('cirq_google.engine.qcs_notebook.get_engine')
def test_get_qcs_objects_for_notebook_mocked_engine_succeeds(engine_mock):
    """Uses a mocked engine call to test a 'prod' Engine."""
    fake_processor = cg.engine.SimulatedLocalProcessor(
        processor_id='tester', project_name='mock_project', device=cg.Sycamore
    )
    fake_processor2 = cg.engine.SimulatedLocalProcessor(
        processor_id='tester23', project_name='mock_project', device=cg.Sycamore23
    )
    fake_engine = cg.engine.SimulatedLocalEngine([fake_processor, fake_processor2])
    engine_mock.return_value = fake_engine

    result = get_qcs_objects_for_notebook()
    _assert_correct_types(result)
    assert result.signed_in
    assert not result.is_simulator
    assert result.project_id == 'mock_project'
    assert len(result.device.metadata.qubit_set) == 54

    result = get_qcs_objects_for_notebook(processor_id='tester')
    _assert_correct_types(result)
    assert result.signed_in
    assert not result.is_simulator
    assert result.project_id == 'mock_project'
    assert len(result.device.metadata.qubit_set) == 54

    result = get_qcs_objects_for_notebook(processor_id='tester23')
    _assert_correct_types(result)
    assert result.signed_in
    assert not result.is_simulator
    assert result.project_id == 'mock_project'
    assert len(result.device.metadata.qubit_set) == 23


@mock.patch('cirq_google.engine.qcs_notebook.get_engine')
def test_get_qcs_objects_for_notebook_no_processors(engine_mock):
    fake_engine = cg.engine.SimulatedLocalEngine([])
    engine_mock.return_value = fake_engine
    with pytest.raises(ValueError, match='processors'):
        _ = get_qcs_objects_for_notebook()


@mock.patch.dict('sys.modules', {'google.colab': mock.Mock()})
@mock.patch('cirq_google.engine.qcs_notebook.get_engine')
def test_get_qcs_objects_for_notebook_auth_succeeds(engine_mock):
    fake_processor = cg.engine.SimulatedLocalProcessor(
        processor_id='tester', project_name='mock_project', device=cg.Sycamore
    )
    fake_engine = cg.engine.SimulatedLocalEngine([fake_processor])
    engine_mock.return_value = fake_engine
    result = get_qcs_objects_for_notebook()
    _assert_correct_types(result)
    assert result.signed_in
    assert not result.is_simulator
    assert result.project_id == 'mock_project'
    assert len(result.device.metadata.qubit_set) == 54


@mock.patch.dict('sys.modules', {'google.colab': mock.Mock()})
@mock.patch('cirq_google.engine.qcs_notebook.get_engine')
def test_get_qcs_objects_for_notebook_auth_fails(engine_mock):
    auth_mock = sys.modules['google.colab']

    auth_mock.auth.authenticate_user = mock.Mock(side_effect=Exception('mock auth failure'))
    fake_processor = cg.engine.SimulatedLocalProcessor(
        processor_id='tester', project_name='mock_project', device=cg.Sycamore
    )
    fake_engine = cg.engine.SimulatedLocalEngine([fake_processor])
    engine_mock.return_value = fake_engine
    result = get_qcs_objects_for_notebook()

    # Auth failed, default to simulator
    _assert_correct_types(result)
    assert not result.signed_in
    assert result.is_simulator
    assert result.project_id == 'fake_project'


class TestGetHardwareEngineAndAuthenticateUser(unittest.TestCase):
    """Tests for the public API `get_hardware_engine_and_authenticate_user` which
    authenticates the user and returns a production engine instance ."""

    @mock.patch.dict('sys.modules', {'google.colab': mock.Mock()})
    @mock.patch('cirq_google.engine.qcs_notebook.get_engine')
    def test_authentication_success(self, engine_mock):
        fake_processor = cg.engine.SimulatedLocalProcessor(
            processor_id='tester', project_name='mock_project', device=cg.Sycamore
        )
        fake_engine = cg.engine.SimulatedLocalEngine([fake_processor])
        engine_mock.return_value = fake_engine
        project_id = "my-project"

        engine = get_hardware_engine_and_authenticate_user(project_id)

        self.assertIsInstance(engine, AbstractEngine)
        self.assertEqual(engine, fake_engine)

    def test_authentication_failure(self):
        project_id = "invalid-project"

        # Mock authentication failure
        with unittest.mock.patch(
            "cirq_google.engine.qcs_notebook._authenticate_user"
        ) as mock_authenticate_user:
            mock_authenticate_user.side_effect = Exception("mock auth failure")

            with self.assertRaises(
                Exception,
                msg="Authentication failed, you may not have permission to access"
                + " a hardware Engine. Use a virtual Engine instead.",
            ):
                get_hardware_engine_and_authenticate_user(project_id)

    def test_clear_output(self):
        project_id = "my-project"

        with unittest.mock.patch(
            "cirq_google.engine.qcs_notebook._authenticate_user"
        ) as mock_authenticate_user:
            get_hardware_engine_and_authenticate_user(project_id, True)

            mock_authenticate_user.assert_called_with(True)

    def test_no_clear_output(self):
        project_id = "my-project"

        with unittest.mock.patch(
            "cirq_google.engine.qcs_notebook._authenticate_user"
        ) as mock_authenticate_user:
            get_hardware_engine_and_authenticate_user(project_id, False)

            mock_authenticate_user.assert_called_with(False)
