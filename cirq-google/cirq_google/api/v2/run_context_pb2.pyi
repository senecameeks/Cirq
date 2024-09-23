"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import cirq_google.api.v2.program_pb2
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class RunContext(google.protobuf.message.Message):
    """The context for running a quantum program."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMETER_SWEEPS_FIELD_NUMBER: builtins.int
    DEVICE_PARAMETERS_OVERRIDE_FIELD_NUMBER: builtins.int
    @property
    def parameter_sweeps(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ParameterSweep]:
        """The parameters for operations in a program."""

    @property
    def device_parameters_override(self) -> global___DeviceParametersDiff:
        """Optional override of select device parameters before program
        execution. Note it is permissible to specify the same device parameter
        here and in a parameter_sweeps, as sweep.single_sweep.parameter.
        If the same parameter is supplied in both places, the provision here in
        device_parameters_override will have no effect.
        """

    def __init__(
        self,
        *,
        parameter_sweeps: collections.abc.Iterable[global___ParameterSweep] | None = ...,
        device_parameters_override: global___DeviceParametersDiff | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["device_parameters_override", b"device_parameters_override"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["device_parameters_override", b"device_parameters_override", "parameter_sweeps", b"parameter_sweeps"]) -> None: ...

global___RunContext = RunContext

@typing.final
class ParameterSweep(google.protobuf.message.Message):
    """Specifies how to repeatedly sample a circuit, with or without sweeping over
    varying parameter-dicts.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REPETITIONS_FIELD_NUMBER: builtins.int
    SWEEP_FIELD_NUMBER: builtins.int
    repetitions: builtins.int
    """How many times to sample, for each parameter-dict that is swept over.
    This must be set to a value strictly greater than zero.
    """
    @property
    def sweep(self) -> global___Sweep:
        """Which parameters, that control gates in the circuit, to try.

        The keys of the parameters generated by this sweep must be a superset
        of the keys in the program's operation's Args. When this is not specified,
        no parameterization is assumed (and the program must have no
        args with symbols).
        """

    def __init__(
        self,
        *,
        repetitions: builtins.int = ...,
        sweep: global___Sweep | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["sweep", b"sweep"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["repetitions", b"repetitions", "sweep", b"sweep"]) -> None: ...

global___ParameterSweep = ParameterSweep

@typing.final
class Sweep(google.protobuf.message.Message):
    """A sweep over all of the parameters in a program."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SWEEP_FUNCTION_FIELD_NUMBER: builtins.int
    SINGLE_SWEEP_FIELD_NUMBER: builtins.int
    @property
    def sweep_function(self) -> global___SweepFunction: ...
    @property
    def single_sweep(self) -> global___SingleSweep: ...
    def __init__(
        self,
        *,
        sweep_function: global___SweepFunction | None = ...,
        single_sweep: global___SingleSweep | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["single_sweep", b"single_sweep", "sweep", b"sweep", "sweep_function", b"sweep_function"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["single_sweep", b"single_sweep", "sweep", b"sweep", "sweep_function", b"sweep_function"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["sweep", b"sweep"]) -> typing.Literal["sweep_function", "single_sweep"] | None: ...

global___Sweep = Sweep

@typing.final
class SweepFunction(google.protobuf.message.Message):
    """A function that takes multiple sweeps and produces more sweeps."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _FunctionType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _FunctionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SweepFunction._FunctionType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        FUNCTION_TYPE_UNSPECIFIED: SweepFunction._FunctionType.ValueType  # 0
        """The function type is not specified. Should never be used."""
        PRODUCT: SweepFunction._FunctionType.ValueType  # 1
        """A Cartesian product of parameter sweeps.

        Example of product:
        If one of the sweeps assigns
        "a": 0.0
        "a": 1.0
        and another assigns
        "b": 2.0
        "b": 3.0
        then the product of these assigns all possible combinations.
        "a": 0.0, "b": 2.0
        "a": 0.0, "b": 3.0
        "a": 1.0, "b": 2.0
        "a": 1.0, "b": 3.0
        """
        ZIP: SweepFunction._FunctionType.ValueType  # 2
        """A zip product of parameter sweeps.

        Example of zip:
        If one of the sweeps assigns
        "a": 0.0
        "a": 1.0
        and another assigns
        "b": 2.0
        "b": 3.0
        then the product of these assigns
        "a": 0.0, "b": 2.0
        "a": 1.0, "b": 3.0
        Note: if one sweep is shorter, the others will be truncated.
        """

    class FunctionType(_FunctionType, metaclass=_FunctionTypeEnumTypeWrapper):
        """The type of sweep function."""

    FUNCTION_TYPE_UNSPECIFIED: SweepFunction.FunctionType.ValueType  # 0
    """The function type is not specified. Should never be used."""
    PRODUCT: SweepFunction.FunctionType.ValueType  # 1
    """A Cartesian product of parameter sweeps.

    Example of product:
    If one of the sweeps assigns
    "a": 0.0
    "a": 1.0
    and another assigns
    "b": 2.0
    "b": 3.0
    then the product of these assigns all possible combinations.
    "a": 0.0, "b": 2.0
    "a": 0.0, "b": 3.0
    "a": 1.0, "b": 2.0
    "a": 1.0, "b": 3.0
    """
    ZIP: SweepFunction.FunctionType.ValueType  # 2
    """A zip product of parameter sweeps.

    Example of zip:
    If one of the sweeps assigns
    "a": 0.0
    "a": 1.0
    and another assigns
    "b": 2.0
    "b": 3.0
    then the product of these assigns
    "a": 0.0, "b": 2.0
    "a": 1.0, "b": 3.0
    Note: if one sweep is shorter, the others will be truncated.
    """

    FUNCTION_TYPE_FIELD_NUMBER: builtins.int
    SWEEPS_FIELD_NUMBER: builtins.int
    function_type: global___SweepFunction.FunctionType.ValueType
    @property
    def sweeps(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Sweep]:
        """The argument sweeps to the function."""

    def __init__(
        self,
        *,
        function_type: global___SweepFunction.FunctionType.ValueType = ...,
        sweeps: collections.abc.Iterable[global___Sweep] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["function_type", b"function_type", "sweeps", b"sweeps"]) -> None: ...

global___SweepFunction = SweepFunction

@typing.final
class DeviceParameter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    IDX_FIELD_NUMBER: builtins.int
    UNITS_FIELD_NUMBER: builtins.int
    idx: builtins.int
    """If the value is an array, the index of the array to change."""
    units: builtins.str
    """String representation of the units, if any.
    Examples: "GHz", "ns", etc.
    """
    @property
    def path(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Path to the parameter key"""

    def __init__(
        self,
        *,
        path: collections.abc.Iterable[builtins.str] | None = ...,
        idx: builtins.int | None = ...,
        units: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_idx", b"_idx", "_units", b"_units", "idx", b"idx", "units", b"units"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_idx", b"_idx", "_units", b"_units", "idx", b"idx", "path", b"path", "units", b"units"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_idx", b"_idx"]) -> typing.Literal["idx"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_units", b"_units"]) -> typing.Literal["units"] | None: ...

global___DeviceParameter = DeviceParameter

@typing.final
class DeviceParametersDiff(google.protobuf.message.Message):
    """A bundle of multiple DeviceParameters and their values.
    The main use case is to set those parameters with the
    values from this bundle before executing a circuit sweep.
    Note multiple device parameters may have common ancestor paths
    and/or share the same parameter names. A DeviceParametersDiff
    stores the resource groups hierarchy extracted from the DeviceParameters'
    paths and maintains a table of strings; thereby storing ancestor resource
    groups only once, and avoiding repeated storage of common parameter names.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class ResourceGroup(google.protobuf.message.Message):
        """A resource group a device parameter belongs to.
        The identifier of a resource group is DeviceParameter.path without the
        last component.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PARENT_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        parent: builtins.int
        """parent resource group, as an index into the groups repeated field."""
        name: builtins.int
        """as index into the strs repeated field."""
        def __init__(
            self,
            *,
            parent: builtins.int = ...,
            name: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["name", b"name", "parent", b"parent"]) -> None: ...

    @typing.final
    class GenericValue(google.protobuf.message.Message):
        """Param value whose type is not among proto field types supported by
        ArgValue. In other words, it is the responsibility of the client codes
        to enforce the validity and type consistency of this param value.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_DESCRIPTOR_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        type_descriptor: builtins.str
        """Type description of the value representation. Eg. if the following value
        bytes field is a JSON string, type_descriptor can be its JSON namespace;
        or if the following value field is a protobuf serialization, type_descriptor
        can be its protobuf definition URL.
        """
        value: builtins.bytes
        """The value in client's encoding."""
        def __init__(
            self,
            *,
            type_descriptor: builtins.str = ...,
            value: builtins.bytes = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["type_descriptor", b"type_descriptor", "value", b"value"]) -> None: ...

    @typing.final
    class Param(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        RESOURCE_GROUP_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        GENERIC_VALUE_FIELD_NUMBER: builtins.int
        resource_group: builtins.int
        """the resource group hosting this parameter key, as index into groups
        repeated field.
        """
        name: builtins.int
        """name of this param, as index into the strs repeated field."""
        @property
        def value(self) -> cirq_google.api.v2.program_pb2.ArgValue:
            """this param's new value, as message ArgValue to allow types of bool,
            string, double, float and arrays.
            """

        @property
        def generic_value(self) -> global___DeviceParametersDiff.GenericValue:
            """this param's new value, and its type is not among the variants supported
            by ArgValue.
            """

        def __init__(
            self,
            *,
            resource_group: builtins.int = ...,
            name: builtins.int = ...,
            value: cirq_google.api.v2.program_pb2.ArgValue | None = ...,
            generic_value: global___DeviceParametersDiff.GenericValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["generic_value", b"generic_value", "param_val", b"param_val", "value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["generic_value", b"generic_value", "name", b"name", "param_val", b"param_val", "resource_group", b"resource_group", "value", b"value"]) -> None: ...
        def WhichOneof(self, oneof_group: typing.Literal["param_val", b"param_val"]) -> typing.Literal["value", "generic_value"] | None: ...

    GROUPS_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    STRS_FIELD_NUMBER: builtins.int
    @property
    def groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DeviceParametersDiff.ResourceGroup]: ...
    @property
    def params(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DeviceParametersDiff.Param]: ...
    @property
    def strs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of all key, dir, and deletion names in these contents.
        ResourceGroup.name, Param.name, and Deletion.name are indexes into this list.
        """

    def __init__(
        self,
        *,
        groups: collections.abc.Iterable[global___DeviceParametersDiff.ResourceGroup] | None = ...,
        params: collections.abc.Iterable[global___DeviceParametersDiff.Param] | None = ...,
        strs: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["groups", b"groups", "params", b"params", "strs", b"strs"]) -> None: ...

global___DeviceParametersDiff = DeviceParametersDiff

@typing.final
class SingleSweep(google.protobuf.message.Message):
    """A set of values to loop over for a particular parameter."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMETER_KEY_FIELD_NUMBER: builtins.int
    POINTS_FIELD_NUMBER: builtins.int
    LINSPACE_FIELD_NUMBER: builtins.int
    CONST_VALUE_FIELD_NUMBER: builtins.int
    PARAMETER_FIELD_NUMBER: builtins.int
    parameter_key: builtins.str
    """The parameter key being varied. This cannot be the empty string.
    These are must appear as string Args in the quantum program.
    """
    @property
    def points(self) -> global___Points:
        """An explicit list of points to try."""

    @property
    def linspace(self) -> global___Linspace:
        """Uniformly-spaced sampling over a range."""

    @property
    def const_value(self) -> global___ConstValue:
        """A constant value."""

    @property
    def parameter(self) -> global___DeviceParameter:
        """Optional arguments for if this is a device parameter.
        (as opposed to a circuit symbol)
        """

    def __init__(
        self,
        *,
        parameter_key: builtins.str = ...,
        points: global___Points | None = ...,
        linspace: global___Linspace | None = ...,
        const_value: global___ConstValue | None = ...,
        parameter: global___DeviceParameter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["const_value", b"const_value", "linspace", b"linspace", "parameter", b"parameter", "points", b"points", "sweep", b"sweep"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["const_value", b"const_value", "linspace", b"linspace", "parameter", b"parameter", "parameter_key", b"parameter_key", "points", b"points", "sweep", b"sweep"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["sweep", b"sweep"]) -> typing.Literal["points", "linspace", "const_value"] | None: ...

global___SingleSweep = SingleSweep

@typing.final
class Points(google.protobuf.message.Message):
    """A list of explicit values."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POINTS_FIELD_NUMBER: builtins.int
    @property
    def points(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """The values."""

    def __init__(
        self,
        *,
        points: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["points", b"points"]) -> None: ...

global___Points = Points

@typing.final
class Linspace(google.protobuf.message.Message):
    """A range of evenly-spaced values.

    Example: if the first_point is 1.0, the last_point is 2.0 ,
    and the num_points is 5, thi corresponds to the points
      1.0, 1.25, 1.5, 1.75, 2.0
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIRST_POINT_FIELD_NUMBER: builtins.int
    LAST_POINT_FIELD_NUMBER: builtins.int
    NUM_POINTS_FIELD_NUMBER: builtins.int
    first_point: builtins.float
    """The start of the range."""
    last_point: builtins.float
    """The end of the range."""
    num_points: builtins.int
    """The number of points in the range (including first and last). Must be
    greater than zero. If it is 1, the first_point and last_point must be
    the same.
    """
    def __init__(
        self,
        *,
        first_point: builtins.float = ...,
        last_point: builtins.float = ...,
        num_points: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["first_point", b"first_point", "last_point", b"last_point", "num_points", b"num_points"]) -> None: ...

global___Linspace = Linspace

@typing.final
class ConstValue(google.protobuf.message.Message):
    """A constant value."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IS_NONE_FIELD_NUMBER: builtins.int
    FLOAT_VALUE_FIELD_NUMBER: builtins.int
    INT_VALUE_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    is_none: builtins.bool
    """This value should always be true if set, which represent the python None object."""
    float_value: builtins.float
    int_value: builtins.int
    string_value: builtins.str
    def __init__(
        self,
        *,
        is_none: builtins.bool = ...,
        float_value: builtins.float = ...,
        int_value: builtins.int = ...,
        string_value: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["float_value", b"float_value", "int_value", b"int_value", "is_none", b"is_none", "string_value", b"string_value", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["float_value", b"float_value", "int_value", b"int_value", "is_none", b"is_none", "string_value", b"string_value", "value", b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["value", b"value"]) -> typing.Literal["is_none", "float_value", "int_value", "string_value"] | None: ...

global___ConstValue = ConstValue
