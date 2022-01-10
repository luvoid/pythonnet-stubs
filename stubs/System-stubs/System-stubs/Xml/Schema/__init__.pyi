from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, Tuple, TypeVar, Union, overload

from MS.Internal.Xml.XPath import Axis
from System import Array, AsyncCallback, Boolean, DateTime, DateTimeKind, DateTimeOffset, Decimal, Double, Enum, EventArgs, Exception, IAsyncResult, ICloneable, Int32, Int64, IntPtr, MulticastDelegate, Object, Single, String, SystemException, TimeSpan, Type, Uri, ValueType, Void
from System.Collections import ArrayList, CollectionBase, ICollection, IDictionaryEnumerator, IEnumerable, IEnumerator, IList
from System.Collections.Generic import List
from System.IO import Stream, TextReader, TextWriter
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable, SerializationInfo, StreamingContext
from System.Threading.Tasks import Task
from System.Xml import IDtdAttributeInfo, IDtdAttributeListInfo, IDtdDefaultAttributeInfo, IDtdEntityInfo, IDtdInfo, IDtdParserAdapter, IValidationEventHandling, IXmlLineInfo, IXmlNamespaceResolver, PositionInfo, ValidationType, XmlAttribute, XmlNameTable, XmlNamespaceManager, XmlNode, XmlQualifiedName, XmlReader, XmlResolver, XmlTokenizedType, XmlValidatingReaderImpl, XmlWriter
from System.Xml.Serialization import XmlSerializerNamespaces
from System.Xml.XPath import XPathItem

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class ActiveAxis(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentDepth(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def EndElement(self, localname: StringType, URN: StringType) -> BooleanType: ...
    
    def MoveToAttribute(self, localname: StringType, URN: StringType) -> BooleanType: ...
    
    def MoveToStartElement(self, localname: StringType, URN: StringType) -> BooleanType: ...
    
    def get_CurrentDepth(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AllElementsContentValidator(ContentValidator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, contentType: XmlSchemaContentType, size: IntType, isEmptiable: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsEmptiable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def AddElement(self, name: XmlQualifiedName, particle: ObjectType, isEmptiable: BooleanType) -> BooleanType: ...
    
    def CompleteValidation(self, context: ValidationState) -> BooleanType: ...
    
    def ExpectedElements(self, context: ValidationState, isRequiredOnly: BooleanType) -> ArrayList: ...
    
    def ExpectedParticles(self, context: ValidationState, isRequiredOnly: BooleanType, schemaSet: XmlSchemaSet) -> ArrayList: ...
    
    def InitValidation(self, context: ValidationState) -> VoidType: ...
    
    def ValidateElement(self, name: XmlQualifiedName, context: ValidationState, errorCode: IntType) -> Tuple[ObjectType, IntType]: ...
    
    def get_IsEmptiable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Asttree(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, xPath: StringType, isField: BooleanType, nsmgr: XmlNamespaceManager): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompileXPath(self, xPath: StringType, isField: BooleanType, nsmgr: XmlNamespaceManager) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AutoValidator(BaseValidator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reader: XmlValidatingReaderImpl, schemaCollection: XmlSchemaCollection, eventHandling: IValidationEventHandling): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PreserveWhitespace(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def CompleteValidation(self) -> VoidType: ...
    
    def FindId(self, name: StringType) -> ObjectType: ...
    
    def Validate(self) -> VoidType: ...
    
    def get_PreserveWhitespace(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AxisElement(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AxisStack(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, faxis: ForwardAxis, parent: ActiveAxis): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BaseProcessor(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nameTable: XmlNameTable, schemaNames: SchemaNames, eventHandler: ValidationEventHandler): ...
    
    @overload
    def __init__(self, nameTable: XmlNameTable, schemaNames: SchemaNames, eventHandler: ValidationEventHandler, compilationSettings: XmlSchemaCompilationSettings): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BaseValidator(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, other: BaseValidator): ...
    
    @overload
    def __init__(self, reader: XmlValidatingReaderImpl, schemaCollection: XmlSchemaCollection, eventHandling: IValidationEventHandling): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseUri(self) -> Uri: ...
    
    @BaseUri.setter
    def BaseUri(self, value: Uri) -> None: ...
    
    @property
    def DtdInfo(self) -> IDtdInfo: ...
    
    @DtdInfo.setter
    def DtdInfo(self, value: IDtdInfo) -> None: ...
    
    @property
    def EventHandler(self) -> ValidationEventHandler: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def PositionInfo(self) -> PositionInfo: ...
    
    @property
    def PreserveWhitespace(self) -> BooleanType: ...
    
    @property
    def Reader(self) -> XmlValidatingReaderImpl: ...
    
    @property
    def SchemaCollection(self) -> XmlSchemaCollection: ...
    
    @property
    def SchemaInfo(self) -> SchemaInfo: ...
    
    @SchemaInfo.setter
    def SchemaInfo(self, value: SchemaInfo) -> None: ...
    
    @property
    def SchemaNames(self) -> SchemaNames: ...
    
    @property
    def XmlResolver(self) -> XmlResolver: ...
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CompleteValidation(self) -> VoidType: ...
    
    @staticmethod
    def CreateInstance(valType: ValidationType, reader: XmlValidatingReaderImpl, schemaCollection: XmlSchemaCollection, eventHandling: IValidationEventHandling, processIdentityConstraints: BooleanType) -> BaseValidator: ...
    
    def FindId(self, name: StringType) -> ObjectType: ...
    
    def Validate(self) -> VoidType: ...
    
    def ValidateText(self) -> VoidType: ...
    
    def ValidateWhitespace(self) -> VoidType: ...
    
    def get_BaseUri(self) -> Uri: ...
    
    def get_DtdInfo(self) -> IDtdInfo: ...
    
    def get_EventHandler(self) -> ValidationEventHandler: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_PositionInfo(self) -> PositionInfo: ...
    
    def get_PreserveWhitespace(self) -> BooleanType: ...
    
    def get_Reader(self) -> XmlValidatingReaderImpl: ...
    
    def get_SchemaCollection(self) -> XmlSchemaCollection: ...
    
    def get_SchemaInfo(self) -> SchemaInfo: ...
    
    def get_SchemaNames(self) -> SchemaNames: ...
    
    def get_XmlResolver(self) -> XmlResolver: ...
    
    def set_BaseUri(self, value: Uri) -> VoidType: ...
    
    def set_DtdInfo(self, value: IDtdInfo) -> VoidType: ...
    
    def set_SchemaInfo(self, value: SchemaInfo) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BinaryFacetsChecker(FacetsChecker):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BitSet(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, count: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsEmpty(self) -> BooleanType: ...
    
    @property
    def Item(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def And(self, other: BitSet) -> VoidType: ...
    
    @overload
    def Clear(self) -> VoidType: ...
    
    @overload
    def Clear(self, index: IntType) -> VoidType: ...
    
    def Clone(self) -> BitSet: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def Get(self, index: IntType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Intersects(self, other: BitSet) -> BooleanType: ...
    
    def NextSet(self, startFrom: IntType) -> IntType: ...
    
    def Or(self, other: BitSet) -> VoidType: ...
    
    def Set(self, index: IntType) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsEmpty(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ChameleonKey(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ns: StringType, originalSchema: XmlSchema): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ChoiceNode(InteriorNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ConstructPos(self, firstpos: BitSet, lastpos: BitSet, followpos: ArrayType[BitSet]) -> VoidType: ...
    
    def ExpandTree(self, parent: InteriorNode, symbols: SymbolsDictionary, positions: Positions) -> VoidType: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompiledIdentityConstraint(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> CompiledIdentityConstraint: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, constraint: XmlSchemaIdentityConstraint, nsmgr: XmlNamespaceManager): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Fields(self) -> ArrayType[Asttree]: ...
    
    @property
    def Role(self) -> ConstraintRole: ...
    
    @property
    def Selector(self) -> Asttree: ...
    
    # ---------- Methods ---------- #
    
    def get_Fields(self) -> ArrayType[Asttree]: ...
    
    def get_Role(self) -> ConstraintRole: ...
    
    def get_Selector(self) -> Asttree: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class ConstraintRole(Enum):
        Unique: IntType = 0
        Key: IntType = 1
        Keyref: IntType = 2
    


class Compiler(BaseProcessor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, nameTable: XmlNameTable, eventHandler: ValidationEventHandler, schemaForSchema: XmlSchema, compilationSettings: XmlSchemaCompilationSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Execute(self, schemaSet: XmlSchemaSet, schemaCompiledInfo: SchemaInfo) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConstraintStruct(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContentValidator(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Any() -> ContentValidator: ...
    
    @staticmethod
    @property
    def Empty() -> ContentValidator: ...
    
    @staticmethod
    @property
    def Mixed() -> ContentValidator: ...
    
    @staticmethod
    @property
    def TextOnly() -> ContentValidator: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, contentType: XmlSchemaContentType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContentType(self) -> XmlSchemaContentType: ...
    
    @property
    def IsEmptiable(self) -> BooleanType: ...
    
    @property
    def IsOpen(self) -> BooleanType: ...
    
    @IsOpen.setter
    def IsOpen(self, value: BooleanType) -> None: ...
    
    @property
    def PreserveWhitespace(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def AddParticleToExpected(p: XmlSchemaParticle, schemaSet: XmlSchemaSet, particles: ArrayList) -> VoidType: ...
    
    @staticmethod
    @overload
    def AddParticleToExpected(p: XmlSchemaParticle, schemaSet: XmlSchemaSet, particles: ArrayList, _global: BooleanType) -> VoidType: ...
    
    def CompleteValidation(self, context: ValidationState) -> BooleanType: ...
    
    def ExpectedElements(self, context: ValidationState, isRequiredOnly: BooleanType) -> ArrayList: ...
    
    def ExpectedParticles(self, context: ValidationState, isRequiredOnly: BooleanType, schemaSet: XmlSchemaSet) -> ArrayList: ...
    
    def InitValidation(self, context: ValidationState) -> VoidType: ...
    
    def ValidateElement(self, name: XmlQualifiedName, context: ValidationState, errorCode: IntType) -> Tuple[ObjectType, IntType]: ...
    
    def get_ContentType(self) -> XmlSchemaContentType: ...
    
    def get_IsEmptiable(self) -> BooleanType: ...
    
    def get_IsOpen(self) -> BooleanType: ...
    
    def get_PreserveWhitespace(self) -> BooleanType: ...
    
    def set_IsOpen(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DatatypeImplementation(ABC, XmlSchemaDatatype):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def Variety(self) -> XmlSchemaDatatypeVariety: ...
    
    # ---------- Methods ---------- #
    
    def IsDerivedFrom(self, datatype: XmlSchemaDatatype) -> BooleanType: ...
    
    def ParseValue(self, s: StringType, nameTable: XmlNameTable, nsmgr: IXmlNamespaceResolver) -> ObjectType: ...
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_Variety(self) -> XmlSchemaDatatypeVariety: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_ENTITY(Datatype_NCName):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_ENUMERATION(Datatype_NMTOKEN):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    # ---------- Methods ---------- #
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_ID(Datatype_NCName):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_IDREF(Datatype_NCName):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_List(Datatype_anySimpleType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_NCName(Datatype_Name):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_NMTOKEN(Datatype_token):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_NOTATION(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_Name(Datatype_token):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_QName(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_QNameXdr(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def ParseValue(self, s: StringType, nameTable: XmlNameTable, nsmgr: IXmlNamespaceResolver) -> ObjectType: ...
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_anyAtomicType(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_anySimpleType(DatatypeImplementation):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_anyURI(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_base64Binary(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_boolean(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_byte(Datatype_short):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_char(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def ParseValue(self, s: StringType, nameTable: XmlNameTable, nsmgr: IXmlNamespaceResolver) -> ObjectType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_date(Datatype_dateTimeBase):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_dateTime(Datatype_dateTimeBase):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_dateTimeBase(Datatype_anySimpleType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_dateTimeNoTimeZone(Datatype_dateTimeBase):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_dateTimeTimeZone(Datatype_dateTimeBase):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_day(Datatype_dateTimeBase):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_dayTimeDuration(Datatype_duration):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_decimal(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_double(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_doubleXdr(Datatype_double):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ParseValue(self, s: StringType, nameTable: XmlNameTable, nsmgr: IXmlNamespaceResolver) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_duration(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_fixed(Datatype_decimal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ParseValue(self, s: StringType, nameTable: XmlNameTable, nsmgr: IXmlNamespaceResolver) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_float(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_floatXdr(Datatype_float):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ParseValue(self, s: StringType, nameTable: XmlNameTable, nsmgr: IXmlNamespaceResolver) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_hexBinary(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_int(Datatype_long):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_integer(Datatype_decimal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_language(Datatype_token):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_long(Datatype_integer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_month(Datatype_dateTimeBase):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_monthDay(Datatype_dateTimeBase):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_negativeInteger(Datatype_nonPositiveInteger):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_nonNegativeInteger(Datatype_integer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_nonPositiveInteger(Datatype_integer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_normalizedString(Datatype_string):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_normalizedStringV1Compat(Datatype_string):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_positiveInteger(Datatype_nonNegativeInteger):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_short(Datatype_int):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_string(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_time(Datatype_dateTimeBase):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_timeNoTimeZone(Datatype_dateTimeBase):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_timeTimeZone(Datatype_dateTimeBase):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_token(Datatype_normalizedString):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_tokenV1Compat(Datatype_normalizedStringV1Compat):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_union(Datatype_anySimpleType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_unsignedByte(Datatype_unsignedShort):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_unsignedInt(Datatype_unsignedLong):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_unsignedLong(Datatype_nonNegativeInteger):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_unsignedShort(Datatype_unsignedInt):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_untypedAtomicType(Datatype_anyAtomicType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_uuid(Datatype_anySimpleType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ValueType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    def ParseValue(self, s: StringType, nameTable: XmlNameTable, nsmgr: IXmlNamespaceResolver) -> ObjectType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_year(Datatype_dateTimeBase):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_yearMonth(Datatype_dateTimeBase):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Datatype_yearMonthDuration(Datatype_duration):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DateTimeFacetsChecker(FacetsChecker):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DfaContentValidator(ContentValidator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompleteValidation(self, context: ValidationState) -> BooleanType: ...
    
    def ExpectedElements(self, context: ValidationState, isRequiredOnly: BooleanType) -> ArrayList: ...
    
    def ExpectedParticles(self, context: ValidationState, isRequiredOnly: BooleanType, schemaSet: XmlSchemaSet) -> ArrayList: ...
    
    def InitValidation(self, context: ValidationState) -> VoidType: ...
    
    def ValidateElement(self, name: XmlQualifiedName, context: ValidationState, errorCode: IntType) -> Tuple[ObjectType, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DoubleLinkAxis(Axis):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DtdValidator(BaseValidator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def PreserveWhitespace(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CheckDefaultValue(attdef: SchemaAttDef, sinfo: SchemaInfo, eventHandling: IValidationEventHandling, baseUriStr: StringType) -> VoidType: ...
    
    def CompleteValidation(self) -> VoidType: ...
    
    def FindId(self, name: StringType) -> ObjectType: ...
    
    @staticmethod
    def SetDefaultTypedValue(attdef: SchemaAttDef, readerAdapter: IDtdParserAdapter) -> VoidType: ...
    
    def Validate(self) -> VoidType: ...
    
    def get_PreserveWhitespace(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DurationFacetsChecker(FacetsChecker):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FacetsChecker(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ForwardAxis(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, axis: DoubleLinkAxis, isdesorself: BooleanType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdRefNode(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InteriorNode(ABC, SyntaxTreeNode):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LeftChild(self) -> SyntaxTreeNode: ...
    
    @LeftChild.setter
    def LeftChild(self, value: SyntaxTreeNode) -> None: ...
    
    @property
    def RightChild(self) -> SyntaxTreeNode: ...
    
    @RightChild.setter
    def RightChild(self, value: SyntaxTreeNode) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self, positions: Positions) -> SyntaxTreeNode: ...
    
    def ExpandTree(self, parent: InteriorNode, symbols: SymbolsDictionary, positions: Positions) -> VoidType: ...
    
    def get_LeftChild(self) -> SyntaxTreeNode: ...
    
    def get_RightChild(self) -> SyntaxTreeNode: ...
    
    def set_LeftChild(self, value: SyntaxTreeNode) -> VoidType: ...
    
    def set_RightChild(self, value: SyntaxTreeNode) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KSStruct(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def depth(self) -> IntType: ...
    
    @depth.setter
    def depth(self, value: IntType) -> None: ...
    
    @property
    def fields(self) -> ArrayType[LocatedActiveAxis]: ...
    
    @fields.setter
    def fields(self, value: ArrayType[LocatedActiveAxis]) -> None: ...
    
    @property
    def ks(self) -> KeySequence: ...
    
    @ks.setter
    def ks(self, value: KeySequence) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ks: KeySequence, dim: IntType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeySequence(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, ks: ArrayType[TypedObject]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> ObjectType: ...
    
    @Item.setter
    def Item(self, value: ObjectType) -> None: ...
    
    @property
    def PosCol(self) -> IntType: ...
    
    @property
    def PosLine(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, other: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Item(self, index: IntType) -> ObjectType: ...
    
    def get_PosCol(self) -> IntType: ...
    
    def get_PosLine(self) -> IntType: ...
    
    def set_Item(self, index: IntType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LeafNode(SyntaxTreeNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, pos: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    @property
    def Pos(self) -> IntType: ...
    
    @Pos.setter
    def Pos(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self, positions: Positions) -> SyntaxTreeNode: ...
    
    def ConstructPos(self, firstpos: BitSet, lastpos: BitSet, followpos: ArrayType[BitSet]) -> VoidType: ...
    
    def ExpandTree(self, parent: InteriorNode, symbols: SymbolsDictionary, positions: Positions) -> VoidType: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    def get_Pos(self) -> IntType: ...
    
    def set_Pos(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LeafRangeNode(LeafNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, min: DecimalType, max: DecimalType): ...
    
    @overload
    def __init__(self, pos: IntType, min: DecimalType, max: DecimalType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsRangeNode(self) -> BooleanType: ...
    
    @property
    def Max(self) -> DecimalType: ...
    
    @property
    def Min(self) -> DecimalType: ...
    
    @property
    def NextIteration(self) -> BitSet: ...
    
    @NextIteration.setter
    def NextIteration(self, value: BitSet) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self, positions: Positions) -> SyntaxTreeNode: ...
    
    def ExpandTree(self, parent: InteriorNode, symbols: SymbolsDictionary, positions: Positions) -> VoidType: ...
    
    def get_IsRangeNode(self) -> BooleanType: ...
    
    def get_Max(self) -> DecimalType: ...
    
    def get_Min(self) -> DecimalType: ...
    
    def get_NextIteration(self) -> BitSet: ...
    
    def set_NextIteration(self, value: BitSet) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ListFacetsChecker(FacetsChecker):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocatedActiveAxis(ActiveAxis):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MiscFacetsChecker(FacetsChecker):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NamespaceList(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, namespaces: StringType, targetNamespace: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Enumerate(self) -> ICollection: ...
    
    @property
    def Excluded(self) -> StringType: ...
    
    @property
    def Type(self) -> ListType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Allows(self, ns: StringType) -> BooleanType: ...
    
    @overload
    def Allows(self, qname: XmlQualifiedName) -> BooleanType: ...
    
    def Clone(self) -> NamespaceList: ...
    
    @staticmethod
    def Intersection(o1: NamespaceList, o2: NamespaceList, v1Compat: BooleanType) -> NamespaceList: ...
    
    def IsEmpty(self) -> BooleanType: ...
    
    @staticmethod
    def IsSubset(sub: NamespaceList, super: NamespaceList) -> BooleanType: ...
    
    def ToString(self) -> StringType: ...
    
    @staticmethod
    def Union(o1: NamespaceList, o2: NamespaceList, v1Compat: BooleanType) -> NamespaceList: ...
    
    def get_Enumerate(self) -> ICollection: ...
    
    def get_Excluded(self) -> StringType: ...
    
    def get_Type(self) -> ListType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class ListType(Enum):
        Any: IntType = 0
        Other: IntType = 1
        Set: IntType = 2
    


class NamespaceListNode(SyntaxTreeNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, namespaceList: NamespaceList, particle: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self, positions: Positions) -> SyntaxTreeNode: ...
    
    def ConstructPos(self, firstpos: BitSet, lastpos: BitSet, followpos: ArrayType[BitSet]) -> VoidType: ...
    
    def ExpandTree(self, parent: InteriorNode, symbols: SymbolsDictionary, positions: Positions) -> VoidType: ...
    
    def GetResolvedSymbols(self, symbols: SymbolsDictionary) -> ICollection: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NamespaceListV1Compat(NamespaceList):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, namespaces: StringType, targetNamespace: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Allows(self, ns: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NfaContentValidator(ContentValidator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompleteValidation(self, context: ValidationState) -> BooleanType: ...
    
    def ExpectedElements(self, context: ValidationState, isRequiredOnly: BooleanType) -> ArrayList: ...
    
    def ExpectedParticles(self, context: ValidationState, isRequiredOnly: BooleanType, schemaSet: XmlSchemaSet) -> ArrayList: ...
    
    def InitValidation(self, context: ValidationState) -> VoidType: ...
    
    def ValidateElement(self, name: XmlQualifiedName, context: ValidationState, errorCode: IntType) -> Tuple[ObjectType, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Numeric10FacetsChecker(FacetsChecker):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Numeric2FacetsChecker(FacetsChecker):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Parser(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, schemaType: SchemaType, nameTable: XmlNameTable, schemaNames: SchemaNames, eventHandler: ValidationEventHandler): ...
    
    # ---------- Properties ---------- #
    
    @property
    def XdrSchema(self) -> SchemaInfo: ...
    
    @property
    def XmlSchema(self) -> XmlSchema: ...
    
    # ---------- Methods ---------- #
    
    def FinishParsing(self) -> SchemaType: ...
    
    def Parse(self, reader: XmlReader, targetNamespace: StringType) -> SchemaType: ...
    
    def ParseAsync(self, reader: XmlReader, targetNamespace: StringType) -> Task[SchemaType]: ...
    
    def ParseReaderNode(self) -> BooleanType: ...
    
    def StartParsing(self, reader: XmlReader, targetNamespace: StringType) -> VoidType: ...
    
    def StartParsingAsync(self, reader: XmlReader, targetNamespace: StringType) -> Task: ...
    
    def get_XdrSchema(self) -> SchemaInfo: ...
    
    def get_XmlSchema(self) -> XmlSchema: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ParticleContentValidator(ContentValidator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, contentType: XmlSchemaContentType): ...
    
    @overload
    def __init__(self, contentType: XmlSchemaContentType, enableUpaCheck: BooleanType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddChoice(self) -> VoidType: ...
    
    def AddLeafRange(self, min: DecimalType, max: DecimalType) -> VoidType: ...
    
    def AddName(self, name: XmlQualifiedName, particle: ObjectType) -> VoidType: ...
    
    def AddNamespaceList(self, namespaceList: NamespaceList, particle: ObjectType) -> VoidType: ...
    
    def AddPlus(self) -> VoidType: ...
    
    def AddQMark(self) -> VoidType: ...
    
    def AddSequence(self) -> VoidType: ...
    
    def AddStar(self) -> VoidType: ...
    
    def CloseGroup(self) -> VoidType: ...
    
    def CompleteValidation(self, context: ValidationState) -> BooleanType: ...
    
    def Exists(self, name: XmlQualifiedName) -> BooleanType: ...
    
    @overload
    def Finish(self, useDFA: BooleanType) -> ContentValidator: ...
    
    @overload
    def Finish(self) -> ContentValidator: ...
    
    def InitValidation(self, context: ValidationState) -> VoidType: ...
    
    def OpenGroup(self) -> VoidType: ...
    
    def Start(self) -> VoidType: ...
    
    def ValidateElement(self, name: XmlQualifiedName, context: ValidationState, errorCode: IntType) -> Tuple[ObjectType, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PlusNode(InteriorNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ConstructPos(self, firstpos: BitSet, lastpos: BitSet, followpos: ArrayType[BitSet]) -> VoidType: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Positions(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> Position: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, symbol: IntType, particle: ObjectType) -> IntType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, pos: IntType) -> Position: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Preprocessor(BaseProcessor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, nameTable: XmlNameTable, schemaNames: SchemaNames, eventHandler: ValidationEventHandler): ...
    
    @overload
    def __init__(self, nameTable: XmlNameTable, schemaNames: SchemaNames, eventHandler: ValidationEventHandler, compilationSettings: XmlSchemaCompilationSettings): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Execute(self, schema: XmlSchema, targetNamespace: StringType, loadExternals: BooleanType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QNameFacetsChecker(FacetsChecker):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QmarkNode(InteriorNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ConstructPos(self, firstpos: BitSet, lastpos: BitSet, followpos: ArrayType[BitSet]) -> VoidType: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RangeContentValidator(ContentValidator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompleteValidation(self, context: ValidationState) -> BooleanType: ...
    
    def ExpectedElements(self, context: ValidationState, isRequiredOnly: BooleanType) -> ArrayList: ...
    
    def ExpectedParticles(self, context: ValidationState, isRequiredOnly: BooleanType, schemaSet: XmlSchemaSet) -> ArrayList: ...
    
    def InitValidation(self, context: ValidationState) -> VoidType: ...
    
    def ValidateElement(self, name: XmlQualifiedName, context: ValidationState, errorCode: IntType) -> Tuple[ObjectType, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RedefineEntry(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, external: XmlSchemaRedefine, schema: XmlSchema): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RestrictionFacets(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaAttDef(SchemaDeclBase, IDtdDefaultAttributeInfo, IDtdAttributeInfo):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> SchemaAttDef: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: XmlQualifiedName, prefix: StringType): ...
    
    @overload
    def __init__(self, name: XmlQualifiedName): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaBuilder(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaCollectionCompiler(BaseProcessor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, nameTable: XmlNameTable, eventHandler: ValidationEventHandler): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Execute(self, schema: XmlSchema, schemaInfo: SchemaInfo, compileContentModel: BooleanType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaCollectionPreprocessor(BaseProcessor):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, nameTable: XmlNameTable, schemaNames: SchemaNames, eventHandler: ValidationEventHandler): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Execute(self, schema: XmlSchema, targetNamespace: StringType, loadExternals: BooleanType, xsc: XmlSchemaCollection) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaDeclBase(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaElementDecl(SchemaDeclBase, IDtdAttributeListInfo):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaEntity(ObjectType, IDtdEntityInfo):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaInfo(ObjectType, IDtdInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DocTypeName(self) -> XmlQualifiedName: ...
    
    @DocTypeName.setter
    def DocTypeName(self, value: XmlQualifiedName) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_DocTypeName(self) -> XmlQualifiedName: ...
    
    def set_DocTypeName(self, value: XmlQualifiedName) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaNames(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def NsDataType(self) -> StringType: ...
    
    @NsDataType.setter
    def NsDataType(self, value: StringType) -> None: ...
    
    @property
    def NsDataTypeAlias(self) -> StringType: ...
    
    @NsDataTypeAlias.setter
    def NsDataTypeAlias(self, value: StringType) -> None: ...
    
    @property
    def NsDataTypeOld(self) -> StringType: ...
    
    @NsDataTypeOld.setter
    def NsDataTypeOld(self, value: StringType) -> None: ...
    
    @property
    def NsXdr(self) -> StringType: ...
    
    @NsXdr.setter
    def NsXdr(self, value: StringType) -> None: ...
    
    @property
    def NsXdrAlias(self) -> StringType: ...
    
    @NsXdrAlias.setter
    def NsXdrAlias(self, value: StringType) -> None: ...
    
    @property
    def NsXml(self) -> StringType: ...
    
    @NsXml.setter
    def NsXml(self, value: StringType) -> None: ...
    
    @property
    def NsXmlNs(self) -> StringType: ...
    
    @NsXmlNs.setter
    def NsXmlNs(self, value: StringType) -> None: ...
    
    @property
    def NsXs(self) -> StringType: ...
    
    @NsXs.setter
    def NsXs(self, value: StringType) -> None: ...
    
    @property
    def NsXsi(self) -> StringType: ...
    
    @NsXsi.setter
    def NsXsi(self, value: StringType) -> None: ...
    
    @property
    def QnAbstract(self) -> XmlQualifiedName: ...
    
    @QnAbstract.setter
    def QnAbstract(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnAttributeFormDefault(self) -> XmlQualifiedName: ...
    
    @QnAttributeFormDefault.setter
    def QnAttributeFormDefault(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnBase(self) -> XmlQualifiedName: ...
    
    @QnBase.setter
    def QnBase(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnBlock(self) -> XmlQualifiedName: ...
    
    @QnBlock.setter
    def QnBlock(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnBlockDefault(self) -> XmlQualifiedName: ...
    
    @QnBlockDefault.setter
    def QnBlockDefault(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnClosed(self) -> XmlQualifiedName: ...
    
    @QnClosed.setter
    def QnClosed(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnContent(self) -> XmlQualifiedName: ...
    
    @QnContent.setter
    def QnContent(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnDefault(self) -> XmlQualifiedName: ...
    
    @QnDefault.setter
    def QnDefault(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnDerivedBy(self) -> XmlQualifiedName: ...
    
    @QnDerivedBy.setter
    def QnDerivedBy(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnDtDt(self) -> XmlQualifiedName: ...
    
    @QnDtDt.setter
    def QnDtDt(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnDtMax(self) -> XmlQualifiedName: ...
    
    @QnDtMax.setter
    def QnDtMax(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnDtMaxExclusive(self) -> XmlQualifiedName: ...
    
    @QnDtMaxExclusive.setter
    def QnDtMaxExclusive(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnDtMaxLength(self) -> XmlQualifiedName: ...
    
    @QnDtMaxLength.setter
    def QnDtMaxLength(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnDtMin(self) -> XmlQualifiedName: ...
    
    @QnDtMin.setter
    def QnDtMin(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnDtMinExclusive(self) -> XmlQualifiedName: ...
    
    @QnDtMinExclusive.setter
    def QnDtMinExclusive(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnDtMinLength(self) -> XmlQualifiedName: ...
    
    @QnDtMinLength.setter
    def QnDtMinLength(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnDtType(self) -> XmlQualifiedName: ...
    
    @QnDtType.setter
    def QnDtType(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnDtValues(self) -> XmlQualifiedName: ...
    
    @QnDtValues.setter
    def QnDtValues(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnElementFormDefault(self) -> XmlQualifiedName: ...
    
    @QnElementFormDefault.setter
    def QnElementFormDefault(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnEltOnly(self) -> XmlQualifiedName: ...
    
    @QnEltOnly.setter
    def QnEltOnly(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnEmpty(self) -> XmlQualifiedName: ...
    
    @QnEmpty.setter
    def QnEmpty(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnEntities(self) -> XmlQualifiedName: ...
    
    @QnEntities.setter
    def QnEntities(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnEntity(self) -> XmlQualifiedName: ...
    
    @QnEntity.setter
    def QnEntity(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnEnumeration(self) -> XmlQualifiedName: ...
    
    @QnEnumeration.setter
    def QnEnumeration(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnFinal(self) -> XmlQualifiedName: ...
    
    @QnFinal.setter
    def QnFinal(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnFinalDefault(self) -> XmlQualifiedName: ...
    
    @QnFinalDefault.setter
    def QnFinalDefault(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnFixed(self) -> XmlQualifiedName: ...
    
    @QnFixed.setter
    def QnFixed(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnForm(self) -> XmlQualifiedName: ...
    
    @QnForm.setter
    def QnForm(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnID(self) -> XmlQualifiedName: ...
    
    @QnID.setter
    def QnID(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnIDRef(self) -> XmlQualifiedName: ...
    
    @QnIDRef.setter
    def QnIDRef(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnIDRefs(self) -> XmlQualifiedName: ...
    
    @QnIDRefs.setter
    def QnIDRefs(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnInfinite(self) -> XmlQualifiedName: ...
    
    @QnInfinite.setter
    def QnInfinite(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnItemType(self) -> XmlQualifiedName: ...
    
    @QnItemType.setter
    def QnItemType(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnMany(self) -> XmlQualifiedName: ...
    
    @QnMany.setter
    def QnMany(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnMaxOccurs(self) -> XmlQualifiedName: ...
    
    @QnMaxOccurs.setter
    def QnMaxOccurs(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnMemberTypes(self) -> XmlQualifiedName: ...
    
    @QnMemberTypes.setter
    def QnMemberTypes(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnMinOccurs(self) -> XmlQualifiedName: ...
    
    @QnMinOccurs.setter
    def QnMinOccurs(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnMixed(self) -> XmlQualifiedName: ...
    
    @QnMixed.setter
    def QnMixed(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnModel(self) -> XmlQualifiedName: ...
    
    @QnModel.setter
    def QnModel(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnName(self) -> XmlQualifiedName: ...
    
    @QnName.setter
    def QnName(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnNamespace(self) -> XmlQualifiedName: ...
    
    @QnNamespace.setter
    def QnNamespace(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnNillable(self) -> XmlQualifiedName: ...
    
    @QnNillable.setter
    def QnNillable(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnNmToken(self) -> XmlQualifiedName: ...
    
    @QnNmToken.setter
    def QnNmToken(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnNmTokens(self) -> XmlQualifiedName: ...
    
    @QnNmTokens.setter
    def QnNmTokens(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnNo(self) -> XmlQualifiedName: ...
    
    @QnNo.setter
    def QnNo(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnOne(self) -> XmlQualifiedName: ...
    
    @QnOne.setter
    def QnOne(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnOpen(self) -> XmlQualifiedName: ...
    
    @QnOpen.setter
    def QnOpen(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnOrder(self) -> XmlQualifiedName: ...
    
    @QnOrder.setter
    def QnOrder(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnPCData(self) -> XmlQualifiedName: ...
    
    @QnPCData.setter
    def QnPCData(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnProcessContents(self) -> XmlQualifiedName: ...
    
    @QnProcessContents.setter
    def QnProcessContents(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnPublic(self) -> XmlQualifiedName: ...
    
    @QnPublic.setter
    def QnPublic(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnRef(self) -> XmlQualifiedName: ...
    
    @QnRef.setter
    def QnRef(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnRefer(self) -> XmlQualifiedName: ...
    
    @QnRefer.setter
    def QnRefer(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnRequired(self) -> XmlQualifiedName: ...
    
    @QnRequired.setter
    def QnRequired(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnSchemaLocation(self) -> XmlQualifiedName: ...
    
    @QnSchemaLocation.setter
    def QnSchemaLocation(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnSeq(self) -> XmlQualifiedName: ...
    
    @QnSeq.setter
    def QnSeq(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnSource(self) -> XmlQualifiedName: ...
    
    @QnSource.setter
    def QnSource(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnString(self) -> XmlQualifiedName: ...
    
    @QnString.setter
    def QnString(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnSubstitutionGroup(self) -> XmlQualifiedName: ...
    
    @QnSubstitutionGroup.setter
    def QnSubstitutionGroup(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnSystem(self) -> XmlQualifiedName: ...
    
    @QnSystem.setter
    def QnSystem(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnTargetNamespace(self) -> XmlQualifiedName: ...
    
    @QnTargetNamespace.setter
    def QnTargetNamespace(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnTextOnly(self) -> XmlQualifiedName: ...
    
    @QnTextOnly.setter
    def QnTextOnly(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnType(self) -> XmlQualifiedName: ...
    
    @QnType.setter
    def QnType(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnUse(self) -> XmlQualifiedName: ...
    
    @QnUse.setter
    def QnUse(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnValue(self) -> XmlQualifiedName: ...
    
    @QnValue.setter
    def QnValue(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnVersion(self) -> XmlQualifiedName: ...
    
    @QnVersion.setter
    def QnVersion(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXPath(self) -> XmlQualifiedName: ...
    
    @QnXPath.setter
    def QnXPath(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXdrAliasSchema(self) -> XmlQualifiedName: ...
    
    @QnXdrAliasSchema.setter
    def QnXdrAliasSchema(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXdrAttribute(self) -> XmlQualifiedName: ...
    
    @QnXdrAttribute.setter
    def QnXdrAttribute(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXdrAttributeType(self) -> XmlQualifiedName: ...
    
    @QnXdrAttributeType.setter
    def QnXdrAttributeType(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXdrDataType(self) -> XmlQualifiedName: ...
    
    @QnXdrDataType.setter
    def QnXdrDataType(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXdrDescription(self) -> XmlQualifiedName: ...
    
    @QnXdrDescription.setter
    def QnXdrDescription(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXdrElement(self) -> XmlQualifiedName: ...
    
    @QnXdrElement.setter
    def QnXdrElement(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXdrElementType(self) -> XmlQualifiedName: ...
    
    @QnXdrElementType.setter
    def QnXdrElementType(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXdrExtends(self) -> XmlQualifiedName: ...
    
    @QnXdrExtends.setter
    def QnXdrExtends(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXdrGroup(self) -> XmlQualifiedName: ...
    
    @QnXdrGroup.setter
    def QnXdrGroup(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXdrSchema(self) -> XmlQualifiedName: ...
    
    @QnXdrSchema.setter
    def QnXdrSchema(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXml(self) -> XmlQualifiedName: ...
    
    @QnXml.setter
    def QnXml(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXmlLang(self) -> XmlQualifiedName: ...
    
    @QnXmlLang.setter
    def QnXmlLang(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXmlNs(self) -> XmlQualifiedName: ...
    
    @QnXmlNs.setter
    def QnXmlNs(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdAll(self) -> XmlQualifiedName: ...
    
    @QnXsdAll.setter
    def QnXsdAll(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdAnnotation(self) -> XmlQualifiedName: ...
    
    @QnXsdAnnotation.setter
    def QnXsdAnnotation(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdAny(self) -> XmlQualifiedName: ...
    
    @QnXsdAny.setter
    def QnXsdAny(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdAnyAttribute(self) -> XmlQualifiedName: ...
    
    @QnXsdAnyAttribute.setter
    def QnXsdAnyAttribute(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdAnyType(self) -> XmlQualifiedName: ...
    
    @QnXsdAnyType.setter
    def QnXsdAnyType(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdAppinfo(self) -> XmlQualifiedName: ...
    
    @QnXsdAppinfo.setter
    def QnXsdAppinfo(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdAttribute(self) -> XmlQualifiedName: ...
    
    @QnXsdAttribute.setter
    def QnXsdAttribute(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdAttributeGroup(self) -> XmlQualifiedName: ...
    
    @QnXsdAttributeGroup.setter
    def QnXsdAttributeGroup(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdChoice(self) -> XmlQualifiedName: ...
    
    @QnXsdChoice.setter
    def QnXsdChoice(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdComplexContent(self) -> XmlQualifiedName: ...
    
    @QnXsdComplexContent.setter
    def QnXsdComplexContent(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdComplexType(self) -> XmlQualifiedName: ...
    
    @QnXsdComplexType.setter
    def QnXsdComplexType(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdDocumentation(self) -> XmlQualifiedName: ...
    
    @QnXsdDocumentation.setter
    def QnXsdDocumentation(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdElement(self) -> XmlQualifiedName: ...
    
    @QnXsdElement.setter
    def QnXsdElement(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdEnumeration(self) -> XmlQualifiedName: ...
    
    @QnXsdEnumeration.setter
    def QnXsdEnumeration(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdExtension(self) -> XmlQualifiedName: ...
    
    @QnXsdExtension.setter
    def QnXsdExtension(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdField(self) -> XmlQualifiedName: ...
    
    @QnXsdField.setter
    def QnXsdField(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdFractionDigits(self) -> XmlQualifiedName: ...
    
    @QnXsdFractionDigits.setter
    def QnXsdFractionDigits(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdGroup(self) -> XmlQualifiedName: ...
    
    @QnXsdGroup.setter
    def QnXsdGroup(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdImport(self) -> XmlQualifiedName: ...
    
    @QnXsdImport.setter
    def QnXsdImport(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdInclude(self) -> XmlQualifiedName: ...
    
    @QnXsdInclude.setter
    def QnXsdInclude(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdKey(self) -> XmlQualifiedName: ...
    
    @QnXsdKey.setter
    def QnXsdKey(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdKeyRef(self) -> XmlQualifiedName: ...
    
    @QnXsdKeyRef.setter
    def QnXsdKeyRef(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdLength(self) -> XmlQualifiedName: ...
    
    @QnXsdLength.setter
    def QnXsdLength(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdList(self) -> XmlQualifiedName: ...
    
    @QnXsdList.setter
    def QnXsdList(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdMaxExclusive(self) -> XmlQualifiedName: ...
    
    @QnXsdMaxExclusive.setter
    def QnXsdMaxExclusive(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdMaxInclusive(self) -> XmlQualifiedName: ...
    
    @QnXsdMaxInclusive.setter
    def QnXsdMaxInclusive(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdMaxLength(self) -> XmlQualifiedName: ...
    
    @QnXsdMaxLength.setter
    def QnXsdMaxLength(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdMinExclusive(self) -> XmlQualifiedName: ...
    
    @QnXsdMinExclusive.setter
    def QnXsdMinExclusive(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdMinInclusive(self) -> XmlQualifiedName: ...
    
    @QnXsdMinInclusive.setter
    def QnXsdMinInclusive(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdMinLength(self) -> XmlQualifiedName: ...
    
    @QnXsdMinLength.setter
    def QnXsdMinLength(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdNotation(self) -> XmlQualifiedName: ...
    
    @QnXsdNotation.setter
    def QnXsdNotation(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdPattern(self) -> XmlQualifiedName: ...
    
    @QnXsdPattern.setter
    def QnXsdPattern(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdRedefine(self) -> XmlQualifiedName: ...
    
    @QnXsdRedefine.setter
    def QnXsdRedefine(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdRestriction(self) -> XmlQualifiedName: ...
    
    @QnXsdRestriction.setter
    def QnXsdRestriction(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdSchema(self) -> XmlQualifiedName: ...
    
    @QnXsdSchema.setter
    def QnXsdSchema(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdSelector(self) -> XmlQualifiedName: ...
    
    @QnXsdSelector.setter
    def QnXsdSelector(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdSequence(self) -> XmlQualifiedName: ...
    
    @QnXsdSequence.setter
    def QnXsdSequence(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdSimpleContent(self) -> XmlQualifiedName: ...
    
    @QnXsdSimpleContent.setter
    def QnXsdSimpleContent(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdSimpleType(self) -> XmlQualifiedName: ...
    
    @QnXsdSimpleType.setter
    def QnXsdSimpleType(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdTotalDigits(self) -> XmlQualifiedName: ...
    
    @QnXsdTotalDigits.setter
    def QnXsdTotalDigits(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdUnion(self) -> XmlQualifiedName: ...
    
    @QnXsdUnion.setter
    def QnXsdUnion(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdUnique(self) -> XmlQualifiedName: ...
    
    @QnXsdUnique.setter
    def QnXsdUnique(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnXsdWhiteSpace(self) -> XmlQualifiedName: ...
    
    @QnXsdWhiteSpace.setter
    def QnXsdWhiteSpace(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def QnYes(self) -> XmlQualifiedName: ...
    
    @QnYes.setter
    def QnYes(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def XdrSchema(self) -> StringType: ...
    
    @XdrSchema.setter
    def XdrSchema(self, value: StringType) -> None: ...
    
    @property
    def XsdSchema(self) -> StringType: ...
    
    @XsdSchema.setter
    def XsdSchema(self, value: StringType) -> None: ...
    
    @property
    def XsiNil(self) -> StringType: ...
    
    @XsiNil.setter
    def XsiNil(self, value: StringType) -> None: ...
    
    @property
    def XsiNoNamespaceSchemaLocation(self) -> StringType: ...
    
    @XsiNoNamespaceSchemaLocation.setter
    def XsiNoNamespaceSchemaLocation(self, value: StringType) -> None: ...
    
    @property
    def XsiSchemaLocation(self) -> StringType: ...
    
    @XsiSchemaLocation.setter
    def XsiSchemaLocation(self, value: StringType) -> None: ...
    
    @property
    def XsiType(self) -> StringType: ...
    
    @XsiType.setter
    def XsiType(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, nameTable: XmlNameTable): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    # ---------- Methods ---------- #
    
    def CreateTokenToQNameTable(self) -> VoidType: ...
    
    def GetName(self, token: Token) -> XmlQualifiedName: ...
    
    def IsXDRRoot(self, localName: StringType, ns: StringType) -> BooleanType: ...
    
    def IsXSDRoot(self, localName: StringType, ns: StringType) -> BooleanType: ...
    
    def SchemaTypeFromRoot(self, localName: StringType, ns: StringType) -> SchemaType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class Token(Enum):
        Empty: IntType = 0
        SchemaName: IntType = 1
        SchemaType: IntType = 2
        SchemaMaxOccurs: IntType = 3
        SchemaMinOccurs: IntType = 4
        SchemaInfinite: IntType = 5
        SchemaModel: IntType = 6
        SchemaOpen: IntType = 7
        SchemaClosed: IntType = 8
        SchemaContent: IntType = 9
        SchemaMixed: IntType = 10
        SchemaEmpty: IntType = 11
        SchemaElementOnly: IntType = 12
        SchemaTextOnly: IntType = 13
        SchemaOrder: IntType = 14
        SchemaSeq: IntType = 15
        SchemaOne: IntType = 16
        SchemaMany: IntType = 17
        SchemaRequired: IntType = 18
        SchemaYes: IntType = 19
        SchemaNo: IntType = 20
        SchemaString: IntType = 21
        SchemaId: IntType = 22
        SchemaIdref: IntType = 23
        SchemaIdrefs: IntType = 24
        SchemaEntity: IntType = 25
        SchemaEntities: IntType = 26
        SchemaNmtoken: IntType = 27
        SchemaNmtokens: IntType = 28
        SchemaEnumeration: IntType = 29
        SchemaDefault: IntType = 30
        XdrRoot: IntType = 31
        XdrElementType: IntType = 32
        XdrElement: IntType = 33
        XdrGroup: IntType = 34
        XdrAttributeType: IntType = 35
        XdrAttribute: IntType = 36
        XdrDatatype: IntType = 37
        XdrDescription: IntType = 38
        XdrExtends: IntType = 39
        SchemaXdrRootAlias: IntType = 40
        SchemaDtType: IntType = 41
        SchemaDtValues: IntType = 42
        SchemaDtMaxLength: IntType = 43
        SchemaDtMinLength: IntType = 44
        SchemaDtMax: IntType = 45
        SchemaDtMin: IntType = 46
        SchemaDtMinExclusive: IntType = 47
        SchemaDtMaxExclusive: IntType = 48
        SchemaTargetNamespace: IntType = 49
        SchemaVersion: IntType = 50
        SchemaFinalDefault: IntType = 51
        SchemaBlockDefault: IntType = 52
        SchemaFixed: IntType = 53
        SchemaAbstract: IntType = 54
        SchemaBlock: IntType = 55
        SchemaSubstitutionGroup: IntType = 56
        SchemaFinal: IntType = 57
        SchemaNillable: IntType = 58
        SchemaRef: IntType = 59
        SchemaBase: IntType = 60
        SchemaDerivedBy: IntType = 61
        SchemaNamespace: IntType = 62
        SchemaProcessContents: IntType = 63
        SchemaRefer: IntType = 64
        SchemaPublic: IntType = 65
        SchemaSystem: IntType = 66
        SchemaSchemaLocation: IntType = 67
        SchemaValue: IntType = 68
        SchemaSource: IntType = 69
        SchemaAttributeFormDefault: IntType = 70
        SchemaElementFormDefault: IntType = 71
        SchemaUse: IntType = 72
        SchemaForm: IntType = 73
        XsdSchema: IntType = 74
        XsdAnnotation: IntType = 75
        XsdInclude: IntType = 76
        XsdImport: IntType = 77
        XsdElement: IntType = 78
        XsdAttribute: IntType = 79
        xsdAttributeGroup: IntType = 80
        XsdAnyAttribute: IntType = 81
        XsdGroup: IntType = 82
        XsdAll: IntType = 83
        XsdChoice: IntType = 84
        XsdSequence: IntType = 85
        XsdAny: IntType = 86
        XsdNotation: IntType = 87
        XsdSimpleType: IntType = 88
        XsdComplexType: IntType = 89
        XsdUnique: IntType = 90
        XsdKey: IntType = 91
        XsdKeyref: IntType = 92
        XsdSelector: IntType = 93
        XsdField: IntType = 94
        XsdMinExclusive: IntType = 95
        XsdMinInclusive: IntType = 96
        XsdMaxExclusive: IntType = 97
        XsdMaxInclusive: IntType = 98
        XsdTotalDigits: IntType = 99
        XsdFractionDigits: IntType = 100
        XsdLength: IntType = 101
        XsdMinLength: IntType = 102
        XsdMaxLength: IntType = 103
        XsdEnumeration: IntType = 104
        XsdPattern: IntType = 105
        XsdDocumentation: IntType = 106
        XsdAppInfo: IntType = 107
        XsdComplexContent: IntType = 108
        XsdComplexContentExtension: IntType = 109
        XsdComplexContentRestriction: IntType = 110
        XsdSimpleContent: IntType = 111
        XsdSimpleContentExtension: IntType = 112
        XsdSimpleContentRestriction: IntType = 113
        XsdSimpleTypeList: IntType = 114
        XsdSimpleTypeRestriction: IntType = 115
        XsdSimpleTypeUnion: IntType = 116
        XsdWhitespace: IntType = 117
        XsdRedefine: IntType = 118
        SchemaItemType: IntType = 119
        SchemaMemberTypes: IntType = 120
        SchemaXPath: IntType = 121
        XmlLang: IntType = 122
    


class SchemaNamespaceManager(XmlNamespaceManager, IXmlNamespaceResolver, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, node: XmlSchemaObject): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    def LookupPrefix(self, ns: StringType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaNotation(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SelectorActiveAxis(ActiveAxis):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, axisTree: Asttree, cs: ConstraintStruct): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EmptyStack(self) -> BooleanType: ...
    
    @property
    def lastDepth(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def EndElement(self, localname: StringType, URN: StringType) -> BooleanType: ...
    
    def PopKS(self) -> KeySequence: ...
    
    def PushKS(self, errline: IntType, errcol: IntType) -> IntType: ...
    
    def get_EmptyStack(self) -> BooleanType: ...
    
    def get_lastDepth(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SequenceNode(InteriorNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ConstructPos(self, firstpos: BitSet, lastpos: BitSet, followpos: ArrayType[BitSet]) -> VoidType: ...
    
    def ExpandTree(self, parent: InteriorNode, symbols: SymbolsDictionary, positions: Positions) -> VoidType: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StarNode(InteriorNode):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def ConstructPos(self, firstpos: BitSet, lastpos: BitSet, followpos: ArrayType[BitSet]) -> VoidType: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringFacetsChecker(FacetsChecker):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SymbolsDictionary(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def CountOfNames(self) -> IntType: ...
    
    @property
    def IsUpaEnforced(self) -> BooleanType: ...
    
    @IsUpaEnforced.setter
    def IsUpaEnforced(self, value: BooleanType) -> None: ...
    
    @property
    def Item(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def AddName(self, name: XmlQualifiedName, particle: ObjectType) -> IntType: ...
    
    def AddNamespaceList(self, list: NamespaceList, particle: ObjectType, allowLocal: BooleanType) -> VoidType: ...
    
    def Exists(self, name: XmlQualifiedName) -> BooleanType: ...
    
    def GetNamespaceListSymbols(self, list: NamespaceList) -> ICollection: ...
    
    def GetParticle(self, symbol: IntType) -> ObjectType: ...
    
    def NameOf(self, symbol: IntType) -> StringType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_CountOfNames(self) -> IntType: ...
    
    def get_IsUpaEnforced(self) -> BooleanType: ...
    
    def get_Item(self, name: XmlQualifiedName) -> IntType: ...
    
    def set_IsUpaEnforced(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SyntaxTreeNode(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    @property
    def IsRangeNode(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self, positions: Positions) -> SyntaxTreeNode: ...
    
    def ConstructPos(self, firstpos: BitSet, lastpos: BitSet, followpos: ArrayType[BitSet]) -> VoidType: ...
    
    def ExpandTree(self, parent: InteriorNode, symbols: SymbolsDictionary, positions: Positions) -> VoidType: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    def get_IsRangeNode(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypedObject(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, obj: ObjectType, svalue: StringType, xsdtype: XmlSchemaDatatype): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Dim(self) -> IntType: ...
    
    @property
    def Dvalue(self) -> ArrayType[DecimalType]: ...
    
    @property
    def IsDecimal(self) -> BooleanType: ...
    
    @property
    def IsList(self) -> BooleanType: ...
    
    @property
    def Type(self) -> XmlSchemaDatatype: ...
    
    @Type.setter
    def Type(self, value: XmlSchemaDatatype) -> None: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    @Value.setter
    def Value(self, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, other: TypedObject) -> BooleanType: ...
    
    def SetDecimal(self) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Dim(self) -> IntType: ...
    
    def get_Dvalue(self) -> ArrayType[DecimalType]: ...
    
    def get_IsDecimal(self) -> BooleanType: ...
    
    def get_IsList(self) -> BooleanType: ...
    
    def get_Type(self) -> XmlSchemaDatatype: ...
    
    def get_Value(self) -> ObjectType: ...
    
    def set_Type(self, value: XmlSchemaDatatype) -> VoidType: ...
    
    def set_Value(self, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnionFacetsChecker(FacetsChecker):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UpaException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, particle1: ObjectType, particle2: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Particle1(self) -> ObjectType: ...
    
    @property
    def Particle2(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Particle1(self) -> ObjectType: ...
    
    def get_Particle2(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValidationEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Exception(self) -> XmlSchemaException: ...
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def Severity(self) -> XmlSeverityType: ...
    
    # ---------- Methods ---------- #
    
    def get_Exception(self) -> XmlSchemaException: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_Severity(self) -> XmlSeverityType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValidationEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: ValidationEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: ValidationEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ValidationState(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def AllElementsSet(self) -> BitSet: ...
    
    @AllElementsSet.setter
    def AllElementsSet(self, value: BitSet) -> None: ...
    
    @property
    def CheckRequiredAttribute(self) -> BooleanType: ...
    
    @CheckRequiredAttribute.setter
    def CheckRequiredAttribute(self, value: BooleanType) -> None: ...
    
    @property
    def Constr(self) -> ArrayType[ConstraintStruct]: ...
    
    @Constr.setter
    def Constr(self, value: ArrayType[ConstraintStruct]) -> None: ...
    
    @property
    def CurPos(self) -> ArrayType[BitSet]: ...
    
    @CurPos.setter
    def CurPos(self, value: ArrayType[BitSet]) -> None: ...
    
    @property
    def CurrentState(self) -> StateUnion: ...
    
    @CurrentState.setter
    def CurrentState(self, value: StateUnion) -> None: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @Depth.setter
    def Depth(self, value: IntType) -> None: ...
    
    @property
    def ElementDecl(self) -> SchemaElementDecl: ...
    
    @ElementDecl.setter
    def ElementDecl(self, value: SchemaElementDecl) -> None: ...
    
    @property
    def ElementDeclBeforeXsi(self) -> SchemaElementDecl: ...
    
    @ElementDeclBeforeXsi.setter
    def ElementDeclBeforeXsi(self, value: SchemaElementDecl) -> None: ...
    
    @property
    def HasMatched(self) -> BooleanType: ...
    
    @HasMatched.setter
    def HasMatched(self, value: BooleanType) -> None: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @IsDefault.setter
    def IsDefault(self, value: BooleanType) -> None: ...
    
    @property
    def IsNill(self) -> BooleanType: ...
    
    @IsNill.setter
    def IsNill(self, value: BooleanType) -> None: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @LocalName.setter
    def LocalName(self, value: StringType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def NeedValidateChildren(self) -> BooleanType: ...
    
    @NeedValidateChildren.setter
    def NeedValidateChildren(self, value: BooleanType) -> None: ...
    
    @property
    def ProcessContents(self) -> XmlSchemaContentProcessing: ...
    
    @ProcessContents.setter
    def ProcessContents(self, value: XmlSchemaContentProcessing) -> None: ...
    
    @property
    def RunningPositions(self) -> List[RangePositionInfo]: ...
    
    @RunningPositions.setter
    def RunningPositions(self, value: List[RangePositionInfo]) -> None: ...
    
    @property
    def TooComplex(self) -> BooleanType: ...
    
    @TooComplex.setter
    def TooComplex(self, value: BooleanType) -> None: ...
    
    @property
    def ValidationSkipped(self) -> BooleanType: ...
    
    @ValidationSkipped.setter
    def ValidationSkipped(self, value: BooleanType) -> None: ...
    
    @property
    def Validity(self) -> XmlSchemaValidity: ...
    
    @Validity.setter
    def Validity(self, value: XmlSchemaValidity) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XdrBuilder(SchemaBuilder):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XdrValidator(BaseValidator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def PreserveWhitespace(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CheckDefaultValue(value: StringType, attdef: SchemaAttDef, sinfo: SchemaInfo, nsManager: XmlNamespaceManager, NameTable: XmlNameTable, sender: ObjectType, eventhandler: ValidationEventHandler, baseUri: StringType, lineNo: IntType, linePos: IntType) -> VoidType: ...
    
    def CompleteValidation(self) -> VoidType: ...
    
    def FindId(self, name: StringType) -> ObjectType: ...
    
    def Validate(self) -> VoidType: ...
    
    def get_PreserveWhitespace(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAnyConverter(XmlBaseConverter):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AnyAtomic() -> XmlValueConverter: ...
    
    @staticmethod
    @property
    def Item() -> XmlValueConverter: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: BooleanType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DateTime, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DateTimeOffset, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DecimalType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DoubleType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: IntType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: LongType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: FloatType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: StringType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ToBoolean(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, value: ObjectType) -> DateTime: ...
    
    @overload
    def ToDateTimeOffset(self, value: ObjectType) -> DateTimeOffset: ...
    
    @overload
    def ToDecimal(self, value: ObjectType) -> DecimalType: ...
    
    @overload
    def ToDouble(self, value: ObjectType) -> DoubleType: ...
    
    @overload
    def ToInt32(self, value: ObjectType) -> IntType: ...
    
    @overload
    def ToInt64(self, value: ObjectType) -> LongType: ...
    
    @overload
    def ToSingle(self, value: ObjectType) -> FloatType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAnyListConverter(XmlListConverter):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AnyAtomicList() -> XmlValueConverter: ...
    
    @staticmethod
    @property
    def ItemList() -> XmlValueConverter: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAtomicValue(XPathItem, ICloneable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNode(self) -> BooleanType: ...
    
    @property
    def TypedValue(self) -> ObjectType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueAsBoolean(self) -> BooleanType: ...
    
    @property
    def ValueAsDateTime(self) -> DateTime: ...
    
    @property
    def ValueAsDouble(self) -> DoubleType: ...
    
    @property
    def ValueAsInt(self) -> IntType: ...
    
    @property
    def ValueAsLong(self) -> LongType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlType(self) -> XmlSchemaType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XmlAtomicValue: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ValueAs(self, type: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def get_IsNode(self) -> BooleanType: ...
    
    def get_TypedValue(self) -> ObjectType: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueAsBoolean(self) -> BooleanType: ...
    
    def get_ValueAsDateTime(self) -> DateTime: ...
    
    def get_ValueAsDouble(self) -> DoubleType: ...
    
    def get_ValueAsInt(self) -> IntType: ...
    
    def get_ValueAsLong(self) -> LongType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlType(self) -> XmlSchemaType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlBaseConverter(ABC, XmlValueConverter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: BooleanType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DateTime, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DateTimeOffset, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DecimalType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DoubleType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: IntType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: LongType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: FloatType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: StringType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: StringType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ToBoolean(self, value: BooleanType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: DateTime) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: DateTimeOffset) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: DecimalType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: DoubleType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: IntType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: LongType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: FloatType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: StringType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, value: BooleanType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: DateTime) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: DateTimeOffset) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: DecimalType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: DoubleType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: IntType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: LongType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: FloatType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: StringType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: ObjectType) -> DateTime: ...
    
    @overload
    def ToDateTimeOffset(self, value: BooleanType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: DateTime) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: DateTimeOffset) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: DecimalType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: DoubleType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: IntType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: LongType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: FloatType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: StringType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: ObjectType) -> DateTimeOffset: ...
    
    @overload
    def ToDecimal(self, value: BooleanType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: DateTime) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: DateTimeOffset) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: DecimalType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: DoubleType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: IntType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: LongType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: FloatType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: StringType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: ObjectType) -> DecimalType: ...
    
    @overload
    def ToDouble(self, value: BooleanType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: DateTime) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: DateTimeOffset) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: DecimalType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: DoubleType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: IntType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: LongType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: FloatType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: StringType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: ObjectType) -> DoubleType: ...
    
    @overload
    def ToInt32(self, value: BooleanType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: DateTime) -> IntType: ...
    
    @overload
    def ToInt32(self, value: DateTimeOffset) -> IntType: ...
    
    @overload
    def ToInt32(self, value: DecimalType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: DoubleType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: IntType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: LongType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: FloatType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: StringType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: ObjectType) -> IntType: ...
    
    @overload
    def ToInt64(self, value: BooleanType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: DateTime) -> LongType: ...
    
    @overload
    def ToInt64(self, value: DateTimeOffset) -> LongType: ...
    
    @overload
    def ToInt64(self, value: DecimalType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: DoubleType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: IntType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: LongType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: FloatType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: StringType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: ObjectType) -> LongType: ...
    
    @overload
    def ToSingle(self, value: BooleanType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: DateTime) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: DateTimeOffset) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: DecimalType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: DoubleType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: IntType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: LongType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: FloatType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: StringType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: ObjectType) -> FloatType: ...
    
    @overload
    def ToString(self, value: BooleanType) -> StringType: ...
    
    @overload
    def ToString(self, value: DateTime) -> StringType: ...
    
    @overload
    def ToString(self, value: DateTimeOffset) -> StringType: ...
    
    @overload
    def ToString(self, value: DecimalType) -> StringType: ...
    
    @overload
    def ToString(self, value: DoubleType) -> StringType: ...
    
    @overload
    def ToString(self, value: IntType) -> StringType: ...
    
    @overload
    def ToString(self, value: LongType) -> StringType: ...
    
    @overload
    def ToString(self, value: FloatType) -> StringType: ...
    
    @overload
    def ToString(self, value: StringType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    @overload
    def ToString(self, value: ObjectType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    @overload
    def ToString(self, value: StringType) -> StringType: ...
    
    @overload
    def ToString(self, value: ObjectType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlBooleanConverter(XmlBaseConverter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: StringType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: BooleanType, destinationType: TypeType) -> ObjectType: ...
    
    @staticmethod
    def Create(schemaType: XmlSchemaType) -> XmlValueConverter: ...
    
    @overload
    def ToBoolean(self, value: BooleanType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: StringType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def ToString(self, value: StringType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    @overload
    def ToString(self, value: BooleanType) -> StringType: ...
    
    @overload
    def ToString(self, value: ObjectType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlDateTimeConverter(XmlBaseConverter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: DateTime, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DateTimeOffset, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: StringType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @staticmethod
    def Create(schemaType: XmlSchemaType) -> XmlValueConverter: ...
    
    @overload
    def ToDateTime(self, value: DateTime) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: DateTimeOffset) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: StringType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: ObjectType) -> DateTime: ...
    
    @overload
    def ToDateTimeOffset(self, value: DateTime) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: DateTimeOffset) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: StringType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: ObjectType) -> DateTimeOffset: ...
    
    @overload
    def ToString(self, value: DateTime) -> StringType: ...
    
    @overload
    def ToString(self, value: DateTimeOffset) -> StringType: ...
    
    @overload
    def ToString(self, value: StringType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    @overload
    def ToString(self, value: ObjectType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlListConverter(XmlBaseConverter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @staticmethod
    def Create(atomicConverter: XmlValueConverter) -> XmlValueConverter: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlMiscConverter(XmlBaseConverter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: StringType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @staticmethod
    def Create(schemaType: XmlSchemaType) -> XmlValueConverter: ...
    
    @overload
    def ToString(self, value: StringType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    @overload
    def ToString(self, value: ObjectType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeConverter(XmlBaseConverter):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Node() -> XmlValueConverter: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNumeric10Converter(XmlBaseConverter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: DecimalType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: IntType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: LongType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: StringType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @staticmethod
    def Create(schemaType: XmlSchemaType) -> XmlValueConverter: ...
    
    @overload
    def ToDecimal(self, value: DecimalType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: IntType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: LongType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: StringType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: ObjectType) -> DecimalType: ...
    
    @overload
    def ToInt32(self, value: DecimalType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: IntType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: LongType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: StringType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: ObjectType) -> IntType: ...
    
    @overload
    def ToInt64(self, value: DecimalType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: IntType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: LongType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: StringType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: ObjectType) -> LongType: ...
    
    @overload
    def ToString(self, value: DecimalType) -> StringType: ...
    
    @overload
    def ToString(self, value: IntType) -> StringType: ...
    
    @overload
    def ToString(self, value: LongType) -> StringType: ...
    
    @overload
    def ToString(self, value: StringType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    @overload
    def ToString(self, value: ObjectType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNumeric2Converter(XmlBaseConverter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: DoubleType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: FloatType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: StringType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @staticmethod
    def Create(schemaType: XmlSchemaType) -> XmlValueConverter: ...
    
    @overload
    def ToDouble(self, value: DoubleType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: FloatType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: StringType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: ObjectType) -> DoubleType: ...
    
    @overload
    def ToSingle(self, value: DoubleType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: FloatType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: StringType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: ObjectType) -> FloatType: ...
    
    @overload
    def ToString(self, value: DoubleType) -> StringType: ...
    
    @overload
    def ToString(self, value: FloatType) -> StringType: ...
    
    @overload
    def ToString(self, value: StringType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    @overload
    def ToString(self, value: ObjectType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchema(XmlSchemaObject):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def InstanceNamespace() -> StringType: ...
    
    @staticmethod
    @property
    def Namespace() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeFormDefault(self) -> XmlSchemaForm: ...
    
    @AttributeFormDefault.setter
    def AttributeFormDefault(self, value: XmlSchemaForm) -> None: ...
    
    @property
    def AttributeGroups(self) -> XmlSchemaObjectTable: ...
    
    @property
    def Attributes(self) -> XmlSchemaObjectTable: ...
    
    @property
    def BlockDefault(self) -> XmlSchemaDerivationMethod: ...
    
    @BlockDefault.setter
    def BlockDefault(self, value: XmlSchemaDerivationMethod) -> None: ...
    
    @property
    def ElementFormDefault(self) -> XmlSchemaForm: ...
    
    @ElementFormDefault.setter
    def ElementFormDefault(self, value: XmlSchemaForm) -> None: ...
    
    @property
    def Elements(self) -> XmlSchemaObjectTable: ...
    
    @property
    def FinalDefault(self) -> XmlSchemaDerivationMethod: ...
    
    @FinalDefault.setter
    def FinalDefault(self, value: XmlSchemaDerivationMethod) -> None: ...
    
    @property
    def Groups(self) -> XmlSchemaObjectTable: ...
    
    @property
    def Id(self) -> StringType: ...
    
    @Id.setter
    def Id(self, value: StringType) -> None: ...
    
    @property
    def Includes(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def IsCompiled(self) -> BooleanType: ...
    
    @property
    def Items(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def Notations(self) -> XmlSchemaObjectTable: ...
    
    @property
    def SchemaTypes(self) -> XmlSchemaObjectTable: ...
    
    @property
    def TargetNamespace(self) -> StringType: ...
    
    @TargetNamespace.setter
    def TargetNamespace(self, value: StringType) -> None: ...
    
    @property
    def UnhandledAttributes(self) -> ArrayType[XmlAttribute]: ...
    
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, value: ArrayType[XmlAttribute]) -> None: ...
    
    @property
    def Version(self) -> StringType: ...
    
    @Version.setter
    def Version(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Compile(self, validationEventHandler: ValidationEventHandler, resolver: XmlResolver) -> VoidType: ...
    
    @overload
    def Compile(self, validationEventHandler: ValidationEventHandler) -> VoidType: ...
    
    @staticmethod
    @overload
    def Read(reader: TextReader, validationEventHandler: ValidationEventHandler) -> XmlSchema: ...
    
    @staticmethod
    @overload
    def Read(stream: Stream, validationEventHandler: ValidationEventHandler) -> XmlSchema: ...
    
    @staticmethod
    @overload
    def Read(reader: XmlReader, validationEventHandler: ValidationEventHandler) -> XmlSchema: ...
    
    @overload
    def Write(self, stream: Stream) -> VoidType: ...
    
    @overload
    def Write(self, stream: Stream, namespaceManager: XmlNamespaceManager) -> VoidType: ...
    
    @overload
    def Write(self, writer: TextWriter) -> VoidType: ...
    
    @overload
    def Write(self, writer: TextWriter, namespaceManager: XmlNamespaceManager) -> VoidType: ...
    
    @overload
    def Write(self, writer: XmlWriter) -> VoidType: ...
    
    @overload
    def Write(self, writer: XmlWriter, namespaceManager: XmlNamespaceManager) -> VoidType: ...
    
    def get_AttributeFormDefault(self) -> XmlSchemaForm: ...
    
    def get_AttributeGroups(self) -> XmlSchemaObjectTable: ...
    
    def get_Attributes(self) -> XmlSchemaObjectTable: ...
    
    def get_BlockDefault(self) -> XmlSchemaDerivationMethod: ...
    
    def get_ElementFormDefault(self) -> XmlSchemaForm: ...
    
    def get_Elements(self) -> XmlSchemaObjectTable: ...
    
    def get_FinalDefault(self) -> XmlSchemaDerivationMethod: ...
    
    def get_Groups(self) -> XmlSchemaObjectTable: ...
    
    def get_Id(self) -> StringType: ...
    
    def get_Includes(self) -> XmlSchemaObjectCollection: ...
    
    def get_IsCompiled(self) -> BooleanType: ...
    
    def get_Items(self) -> XmlSchemaObjectCollection: ...
    
    def get_Notations(self) -> XmlSchemaObjectTable: ...
    
    def get_SchemaTypes(self) -> XmlSchemaObjectTable: ...
    
    def get_TargetNamespace(self) -> StringType: ...
    
    def get_UnhandledAttributes(self) -> ArrayType[XmlAttribute]: ...
    
    def get_Version(self) -> StringType: ...
    
    def set_AttributeFormDefault(self, value: XmlSchemaForm) -> VoidType: ...
    
    def set_BlockDefault(self, value: XmlSchemaDerivationMethod) -> VoidType: ...
    
    def set_ElementFormDefault(self, value: XmlSchemaForm) -> VoidType: ...
    
    def set_FinalDefault(self, value: XmlSchemaDerivationMethod) -> VoidType: ...
    
    def set_Id(self, value: StringType) -> VoidType: ...
    
    def set_TargetNamespace(self, value: StringType) -> VoidType: ...
    
    def set_UnhandledAttributes(self, value: ArrayType[XmlAttribute]) -> VoidType: ...
    
    def set_Version(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaAll(XmlSchemaGroupBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Items(self) -> XmlSchemaObjectCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Items(self) -> XmlSchemaObjectCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaAnnotated(XmlSchemaObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Annotation(self) -> XmlSchemaAnnotation: ...
    
    @Annotation.setter
    def Annotation(self, value: XmlSchemaAnnotation) -> None: ...
    
    @property
    def Id(self) -> StringType: ...
    
    @Id.setter
    def Id(self, value: StringType) -> None: ...
    
    @property
    def UnhandledAttributes(self) -> ArrayType[XmlAttribute]: ...
    
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, value: ArrayType[XmlAttribute]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Annotation(self) -> XmlSchemaAnnotation: ...
    
    def get_Id(self) -> StringType: ...
    
    def get_UnhandledAttributes(self) -> ArrayType[XmlAttribute]: ...
    
    def set_Annotation(self, value: XmlSchemaAnnotation) -> VoidType: ...
    
    def set_Id(self, value: StringType) -> VoidType: ...
    
    def set_UnhandledAttributes(self, value: ArrayType[XmlAttribute]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaAnnotation(XmlSchemaObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Id(self) -> StringType: ...
    
    @Id.setter
    def Id(self, value: StringType) -> None: ...
    
    @property
    def Items(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def UnhandledAttributes(self) -> ArrayType[XmlAttribute]: ...
    
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, value: ArrayType[XmlAttribute]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Id(self) -> StringType: ...
    
    def get_Items(self) -> XmlSchemaObjectCollection: ...
    
    def get_UnhandledAttributes(self) -> ArrayType[XmlAttribute]: ...
    
    def set_Id(self, value: StringType) -> VoidType: ...
    
    def set_UnhandledAttributes(self, value: ArrayType[XmlAttribute]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaAny(XmlSchemaParticle):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def ProcessContents(self) -> XmlSchemaContentProcessing: ...
    
    @ProcessContents.setter
    def ProcessContents(self, value: XmlSchemaContentProcessing) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Namespace(self) -> StringType: ...
    
    def get_ProcessContents(self) -> XmlSchemaContentProcessing: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_ProcessContents(self, value: XmlSchemaContentProcessing) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaAnyAttribute(XmlSchemaAnnotated):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def ProcessContents(self) -> XmlSchemaContentProcessing: ...
    
    @ProcessContents.setter
    def ProcessContents(self, value: XmlSchemaContentProcessing) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Namespace(self) -> StringType: ...
    
    def get_ProcessContents(self) -> XmlSchemaContentProcessing: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_ProcessContents(self, value: XmlSchemaContentProcessing) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaAppInfo(XmlSchemaObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Markup(self) -> ArrayType[XmlNode]: ...
    
    @Markup.setter
    def Markup(self, value: ArrayType[XmlNode]) -> None: ...
    
    @property
    def Source(self) -> StringType: ...
    
    @Source.setter
    def Source(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Markup(self) -> ArrayType[XmlNode]: ...
    
    def get_Source(self) -> StringType: ...
    
    def set_Markup(self, value: ArrayType[XmlNode]) -> VoidType: ...
    
    def set_Source(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaAttribute(XmlSchemaAnnotated):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeSchemaType(self) -> XmlSchemaSimpleType: ...
    
    @property
    def AttributeType(self) -> ObjectType: ...
    
    @property
    def DefaultValue(self) -> StringType: ...
    
    @DefaultValue.setter
    def DefaultValue(self, value: StringType) -> None: ...
    
    @property
    def FixedValue(self) -> StringType: ...
    
    @FixedValue.setter
    def FixedValue(self, value: StringType) -> None: ...
    
    @property
    def Form(self) -> XmlSchemaForm: ...
    
    @Form.setter
    def Form(self, value: XmlSchemaForm) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def QualifiedName(self) -> XmlQualifiedName: ...
    
    @property
    def RefName(self) -> XmlQualifiedName: ...
    
    @RefName.setter
    def RefName(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def SchemaType(self) -> XmlSchemaSimpleType: ...
    
    @SchemaType.setter
    def SchemaType(self, value: XmlSchemaSimpleType) -> None: ...
    
    @property
    def SchemaTypeName(self) -> XmlQualifiedName: ...
    
    @SchemaTypeName.setter
    def SchemaTypeName(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def Use(self) -> XmlSchemaUse: ...
    
    @Use.setter
    def Use(self, value: XmlSchemaUse) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AttributeSchemaType(self) -> XmlSchemaSimpleType: ...
    
    def get_AttributeType(self) -> ObjectType: ...
    
    def get_DefaultValue(self) -> StringType: ...
    
    def get_FixedValue(self) -> StringType: ...
    
    def get_Form(self) -> XmlSchemaForm: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_QualifiedName(self) -> XmlQualifiedName: ...
    
    def get_RefName(self) -> XmlQualifiedName: ...
    
    def get_SchemaType(self) -> XmlSchemaSimpleType: ...
    
    def get_SchemaTypeName(self) -> XmlQualifiedName: ...
    
    def get_Use(self) -> XmlSchemaUse: ...
    
    def set_DefaultValue(self, value: StringType) -> VoidType: ...
    
    def set_FixedValue(self, value: StringType) -> VoidType: ...
    
    def set_Form(self, value: XmlSchemaForm) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_RefName(self, value: XmlQualifiedName) -> VoidType: ...
    
    def set_SchemaType(self, value: XmlSchemaSimpleType) -> VoidType: ...
    
    def set_SchemaTypeName(self, value: XmlQualifiedName) -> VoidType: ...
    
    def set_Use(self, value: XmlSchemaUse) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaAttributeGroup(XmlSchemaAnnotated):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AnyAttribute(self) -> XmlSchemaAnyAttribute: ...
    
    @AnyAttribute.setter
    def AnyAttribute(self, value: XmlSchemaAnyAttribute) -> None: ...
    
    @property
    def Attributes(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def QualifiedName(self) -> XmlQualifiedName: ...
    
    @property
    def RedefinedAttributeGroup(self) -> XmlSchemaAttributeGroup: ...
    
    # ---------- Methods ---------- #
    
    def get_AnyAttribute(self) -> XmlSchemaAnyAttribute: ...
    
    def get_Attributes(self) -> XmlSchemaObjectCollection: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_QualifiedName(self) -> XmlQualifiedName: ...
    
    def get_RedefinedAttributeGroup(self) -> XmlSchemaAttributeGroup: ...
    
    def set_AnyAttribute(self, value: XmlSchemaAnyAttribute) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaAttributeGroupRef(XmlSchemaAnnotated):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def RefName(self) -> XmlQualifiedName: ...
    
    @RefName.setter
    def RefName(self, value: XmlQualifiedName) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_RefName(self) -> XmlQualifiedName: ...
    
    def set_RefName(self, value: XmlQualifiedName) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaChoice(XmlSchemaGroupBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Items(self) -> XmlSchemaObjectCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Items(self) -> XmlSchemaObjectCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, nametable: XmlNameTable): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> XmlSchema: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, ns: StringType, uri: StringType) -> XmlSchema: ...
    
    @overload
    def Add(self, ns: StringType, reader: XmlReader) -> XmlSchema: ...
    
    @overload
    def Add(self, ns: StringType, reader: XmlReader, resolver: XmlResolver) -> XmlSchema: ...
    
    @overload
    def Add(self, schema: XmlSchema) -> XmlSchema: ...
    
    @overload
    def Add(self, schema: XmlSchema, resolver: XmlResolver) -> XmlSchema: ...
    
    @overload
    def Add(self, schema: XmlSchemaCollection) -> VoidType: ...
    
    @overload
    def Contains(self, schema: XmlSchema) -> BooleanType: ...
    
    @overload
    def Contains(self, ns: StringType) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[XmlSchema], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> XmlSchemaCollectionEnumerator: ...
    
    def add_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, ns: StringType) -> XmlSchema: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def remove_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ValidationEventHandler: EventType[ValidationEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaCollectionEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XmlSchema: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Current(self) -> XmlSchema: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaCollectionNode(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaCompilationSettings(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EnableUpaCheck(self) -> BooleanType: ...
    
    @EnableUpaCheck.setter
    def EnableUpaCheck(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_EnableUpaCheck(self) -> BooleanType: ...
    
    def set_EnableUpaCheck(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaComplexContent(XmlSchemaContentModel):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Content(self) -> XmlSchemaContent: ...
    
    @Content.setter
    def Content(self, value: XmlSchemaContent) -> None: ...
    
    @property
    def IsMixed(self) -> BooleanType: ...
    
    @IsMixed.setter
    def IsMixed(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Content(self) -> XmlSchemaContent: ...
    
    def get_IsMixed(self) -> BooleanType: ...
    
    def set_Content(self, value: XmlSchemaContent) -> VoidType: ...
    
    def set_IsMixed(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaComplexContentExtension(XmlSchemaContent):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AnyAttribute(self) -> XmlSchemaAnyAttribute: ...
    
    @AnyAttribute.setter
    def AnyAttribute(self, value: XmlSchemaAnyAttribute) -> None: ...
    
    @property
    def Attributes(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def BaseTypeName(self) -> XmlQualifiedName: ...
    
    @BaseTypeName.setter
    def BaseTypeName(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def Particle(self) -> XmlSchemaParticle: ...
    
    @Particle.setter
    def Particle(self, value: XmlSchemaParticle) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AnyAttribute(self) -> XmlSchemaAnyAttribute: ...
    
    def get_Attributes(self) -> XmlSchemaObjectCollection: ...
    
    def get_BaseTypeName(self) -> XmlQualifiedName: ...
    
    def get_Particle(self) -> XmlSchemaParticle: ...
    
    def set_AnyAttribute(self, value: XmlSchemaAnyAttribute) -> VoidType: ...
    
    def set_BaseTypeName(self, value: XmlQualifiedName) -> VoidType: ...
    
    def set_Particle(self, value: XmlSchemaParticle) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaComplexContentRestriction(XmlSchemaContent):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AnyAttribute(self) -> XmlSchemaAnyAttribute: ...
    
    @AnyAttribute.setter
    def AnyAttribute(self, value: XmlSchemaAnyAttribute) -> None: ...
    
    @property
    def Attributes(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def BaseTypeName(self) -> XmlQualifiedName: ...
    
    @BaseTypeName.setter
    def BaseTypeName(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def Particle(self) -> XmlSchemaParticle: ...
    
    @Particle.setter
    def Particle(self, value: XmlSchemaParticle) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AnyAttribute(self) -> XmlSchemaAnyAttribute: ...
    
    def get_Attributes(self) -> XmlSchemaObjectCollection: ...
    
    def get_BaseTypeName(self) -> XmlQualifiedName: ...
    
    def get_Particle(self) -> XmlSchemaParticle: ...
    
    def set_AnyAttribute(self, value: XmlSchemaAnyAttribute) -> VoidType: ...
    
    def set_BaseTypeName(self, value: XmlQualifiedName) -> VoidType: ...
    
    def set_Particle(self, value: XmlSchemaParticle) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaComplexType(XmlSchemaType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AnyAttribute(self) -> XmlSchemaAnyAttribute: ...
    
    @AnyAttribute.setter
    def AnyAttribute(self, value: XmlSchemaAnyAttribute) -> None: ...
    
    @property
    def AttributeUses(self) -> XmlSchemaObjectTable: ...
    
    @property
    def AttributeWildcard(self) -> XmlSchemaAnyAttribute: ...
    
    @property
    def Attributes(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def Block(self) -> XmlSchemaDerivationMethod: ...
    
    @Block.setter
    def Block(self, value: XmlSchemaDerivationMethod) -> None: ...
    
    @property
    def BlockResolved(self) -> XmlSchemaDerivationMethod: ...
    
    @property
    def ContentModel(self) -> XmlSchemaContentModel: ...
    
    @ContentModel.setter
    def ContentModel(self, value: XmlSchemaContentModel) -> None: ...
    
    @property
    def ContentType(self) -> XmlSchemaContentType: ...
    
    @property
    def ContentTypeParticle(self) -> XmlSchemaParticle: ...
    
    @property
    def IsAbstract(self) -> BooleanType: ...
    
    @IsAbstract.setter
    def IsAbstract(self, value: BooleanType) -> None: ...
    
    @property
    def IsMixed(self) -> BooleanType: ...
    
    @IsMixed.setter
    def IsMixed(self, value: BooleanType) -> None: ...
    
    @property
    def Particle(self) -> XmlSchemaParticle: ...
    
    @Particle.setter
    def Particle(self, value: XmlSchemaParticle) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AnyAttribute(self) -> XmlSchemaAnyAttribute: ...
    
    def get_AttributeUses(self) -> XmlSchemaObjectTable: ...
    
    def get_AttributeWildcard(self) -> XmlSchemaAnyAttribute: ...
    
    def get_Attributes(self) -> XmlSchemaObjectCollection: ...
    
    def get_Block(self) -> XmlSchemaDerivationMethod: ...
    
    def get_BlockResolved(self) -> XmlSchemaDerivationMethod: ...
    
    def get_ContentModel(self) -> XmlSchemaContentModel: ...
    
    def get_ContentType(self) -> XmlSchemaContentType: ...
    
    def get_ContentTypeParticle(self) -> XmlSchemaParticle: ...
    
    def get_IsAbstract(self) -> BooleanType: ...
    
    def get_IsMixed(self) -> BooleanType: ...
    
    def get_Particle(self) -> XmlSchemaParticle: ...
    
    def set_AnyAttribute(self, value: XmlSchemaAnyAttribute) -> VoidType: ...
    
    def set_Block(self, value: XmlSchemaDerivationMethod) -> VoidType: ...
    
    def set_ContentModel(self, value: XmlSchemaContentModel) -> VoidType: ...
    
    def set_IsAbstract(self, value: BooleanType) -> VoidType: ...
    
    def set_IsMixed(self, value: BooleanType) -> VoidType: ...
    
    def set_Particle(self, value: XmlSchemaParticle) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaContent(ABC, XmlSchemaAnnotated):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaContentModel(ABC, XmlSchemaAnnotated):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Content(self) -> XmlSchemaContent: ...
    
    @Content.setter
    def Content(self, value: XmlSchemaContent) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Content(self) -> XmlSchemaContent: ...
    
    def set_Content(self, value: XmlSchemaContent) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaDatatype(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TokenizedType(self) -> XmlTokenizedType: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def Variety(self) -> XmlSchemaDatatypeVariety: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: ObjectType, targetType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: ObjectType, targetType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def IsDerivedFrom(self, datatype: XmlSchemaDatatype) -> BooleanType: ...
    
    def ParseValue(self, s: StringType, nameTable: XmlNameTable, nsmgr: IXmlNamespaceResolver) -> ObjectType: ...
    
    def get_TokenizedType(self) -> XmlTokenizedType: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_Variety(self) -> XmlSchemaDatatypeVariety: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaDocumentation(XmlSchemaObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Language(self) -> StringType: ...
    
    @Language.setter
    def Language(self, value: StringType) -> None: ...
    
    @property
    def Markup(self) -> ArrayType[XmlNode]: ...
    
    @Markup.setter
    def Markup(self, value: ArrayType[XmlNode]) -> None: ...
    
    @property
    def Source(self) -> StringType: ...
    
    @Source.setter
    def Source(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Language(self) -> StringType: ...
    
    def get_Markup(self) -> ArrayType[XmlNode]: ...
    
    def get_Source(self) -> StringType: ...
    
    def set_Language(self, value: StringType) -> VoidType: ...
    
    def set_Markup(self, value: ArrayType[XmlNode]) -> VoidType: ...
    
    def set_Source(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaElement(XmlSchemaParticle):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Block(self) -> XmlSchemaDerivationMethod: ...
    
    @Block.setter
    def Block(self, value: XmlSchemaDerivationMethod) -> None: ...
    
    @property
    def BlockResolved(self) -> XmlSchemaDerivationMethod: ...
    
    @property
    def Constraints(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def DefaultValue(self) -> StringType: ...
    
    @DefaultValue.setter
    def DefaultValue(self, value: StringType) -> None: ...
    
    @property
    def ElementSchemaType(self) -> XmlSchemaType: ...
    
    @property
    def ElementType(self) -> ObjectType: ...
    
    @property
    def Final(self) -> XmlSchemaDerivationMethod: ...
    
    @Final.setter
    def Final(self, value: XmlSchemaDerivationMethod) -> None: ...
    
    @property
    def FinalResolved(self) -> XmlSchemaDerivationMethod: ...
    
    @property
    def FixedValue(self) -> StringType: ...
    
    @FixedValue.setter
    def FixedValue(self, value: StringType) -> None: ...
    
    @property
    def Form(self) -> XmlSchemaForm: ...
    
    @Form.setter
    def Form(self, value: XmlSchemaForm) -> None: ...
    
    @property
    def IsAbstract(self) -> BooleanType: ...
    
    @IsAbstract.setter
    def IsAbstract(self, value: BooleanType) -> None: ...
    
    @property
    def IsNillable(self) -> BooleanType: ...
    
    @IsNillable.setter
    def IsNillable(self, value: BooleanType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def QualifiedName(self) -> XmlQualifiedName: ...
    
    @property
    def RefName(self) -> XmlQualifiedName: ...
    
    @RefName.setter
    def RefName(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def SchemaType(self) -> XmlSchemaType: ...
    
    @SchemaType.setter
    def SchemaType(self, value: XmlSchemaType) -> None: ...
    
    @property
    def SchemaTypeName(self) -> XmlQualifiedName: ...
    
    @SchemaTypeName.setter
    def SchemaTypeName(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def SubstitutionGroup(self) -> XmlQualifiedName: ...
    
    @SubstitutionGroup.setter
    def SubstitutionGroup(self, value: XmlQualifiedName) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Block(self) -> XmlSchemaDerivationMethod: ...
    
    def get_BlockResolved(self) -> XmlSchemaDerivationMethod: ...
    
    def get_Constraints(self) -> XmlSchemaObjectCollection: ...
    
    def get_DefaultValue(self) -> StringType: ...
    
    def get_ElementSchemaType(self) -> XmlSchemaType: ...
    
    def get_ElementType(self) -> ObjectType: ...
    
    def get_Final(self) -> XmlSchemaDerivationMethod: ...
    
    def get_FinalResolved(self) -> XmlSchemaDerivationMethod: ...
    
    def get_FixedValue(self) -> StringType: ...
    
    def get_Form(self) -> XmlSchemaForm: ...
    
    def get_IsAbstract(self) -> BooleanType: ...
    
    def get_IsNillable(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_QualifiedName(self) -> XmlQualifiedName: ...
    
    def get_RefName(self) -> XmlQualifiedName: ...
    
    def get_SchemaType(self) -> XmlSchemaType: ...
    
    def get_SchemaTypeName(self) -> XmlQualifiedName: ...
    
    def get_SubstitutionGroup(self) -> XmlQualifiedName: ...
    
    def set_Block(self, value: XmlSchemaDerivationMethod) -> VoidType: ...
    
    def set_DefaultValue(self, value: StringType) -> VoidType: ...
    
    def set_Final(self, value: XmlSchemaDerivationMethod) -> VoidType: ...
    
    def set_FixedValue(self, value: StringType) -> VoidType: ...
    
    def set_Form(self, value: XmlSchemaForm) -> VoidType: ...
    
    def set_IsAbstract(self, value: BooleanType) -> VoidType: ...
    
    def set_IsNillable(self, value: BooleanType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_RefName(self, value: XmlQualifiedName) -> VoidType: ...
    
    def set_SchemaType(self, value: XmlSchemaType) -> VoidType: ...
    
    def set_SchemaTypeName(self, value: XmlQualifiedName) -> VoidType: ...
    
    def set_SubstitutionGroup(self, value: XmlQualifiedName) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaEnumerationFacet(XmlSchemaFacet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception, lineNumber: IntType, linePosition: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def SourceSchemaObject(self) -> XmlSchemaObject: ...
    
    @property
    def SourceUri(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_SourceSchemaObject(self) -> XmlSchemaObject: ...
    
    def get_SourceUri(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaExternal(ABC, XmlSchemaObject):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Id(self) -> StringType: ...
    
    @Id.setter
    def Id(self, value: StringType) -> None: ...
    
    @property
    def Schema(self) -> XmlSchema: ...
    
    @Schema.setter
    def Schema(self, value: XmlSchema) -> None: ...
    
    @property
    def SchemaLocation(self) -> StringType: ...
    
    @SchemaLocation.setter
    def SchemaLocation(self, value: StringType) -> None: ...
    
    @property
    def UnhandledAttributes(self) -> ArrayType[XmlAttribute]: ...
    
    @UnhandledAttributes.setter
    def UnhandledAttributes(self, value: ArrayType[XmlAttribute]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Id(self) -> StringType: ...
    
    def get_Schema(self) -> XmlSchema: ...
    
    def get_SchemaLocation(self) -> StringType: ...
    
    def get_UnhandledAttributes(self) -> ArrayType[XmlAttribute]: ...
    
    def set_Id(self, value: StringType) -> VoidType: ...
    
    def set_Schema(self, value: XmlSchema) -> VoidType: ...
    
    def set_SchemaLocation(self, value: StringType) -> VoidType: ...
    
    def set_UnhandledAttributes(self, value: ArrayType[XmlAttribute]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaFacet(ABC, XmlSchemaAnnotated):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsFixed(self) -> BooleanType: ...
    
    @IsFixed.setter
    def IsFixed(self, value: BooleanType) -> None: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @Value.setter
    def Value(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_IsFixed(self) -> BooleanType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_IsFixed(self, value: BooleanType) -> VoidType: ...
    
    def set_Value(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaFractionDigitsFacet(XmlSchemaNumericFacet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaGroup(XmlSchemaAnnotated):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Particle(self) -> XmlSchemaGroupBase: ...
    
    @Particle.setter
    def Particle(self, value: XmlSchemaGroupBase) -> None: ...
    
    @property
    def QualifiedName(self) -> XmlQualifiedName: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_Particle(self) -> XmlSchemaGroupBase: ...
    
    def get_QualifiedName(self) -> XmlQualifiedName: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Particle(self, value: XmlSchemaGroupBase) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaGroupBase(ABC, XmlSchemaParticle):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Items(self) -> XmlSchemaObjectCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Items(self) -> XmlSchemaObjectCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaGroupRef(XmlSchemaParticle):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Particle(self) -> XmlSchemaGroupBase: ...
    
    @property
    def RefName(self) -> XmlQualifiedName: ...
    
    @RefName.setter
    def RefName(self, value: XmlQualifiedName) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Particle(self) -> XmlSchemaGroupBase: ...
    
    def get_RefName(self) -> XmlQualifiedName: ...
    
    def set_RefName(self, value: XmlQualifiedName) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaIdentityConstraint(XmlSchemaAnnotated):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Fields(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def QualifiedName(self) -> XmlQualifiedName: ...
    
    @property
    def Selector(self) -> XmlSchemaXPath: ...
    
    @Selector.setter
    def Selector(self, value: XmlSchemaXPath) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Fields(self) -> XmlSchemaObjectCollection: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_QualifiedName(self) -> XmlQualifiedName: ...
    
    def get_Selector(self) -> XmlSchemaXPath: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Selector(self, value: XmlSchemaXPath) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaImport(XmlSchemaExternal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Annotation(self) -> XmlSchemaAnnotation: ...
    
    @Annotation.setter
    def Annotation(self, value: XmlSchemaAnnotation) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Annotation(self) -> XmlSchemaAnnotation: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def set_Annotation(self, value: XmlSchemaAnnotation) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaInclude(XmlSchemaExternal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Annotation(self) -> XmlSchemaAnnotation: ...
    
    @Annotation.setter
    def Annotation(self, value: XmlSchemaAnnotation) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Annotation(self) -> XmlSchemaAnnotation: ...
    
    def set_Annotation(self, value: XmlSchemaAnnotation) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaInference(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Occurrence(self) -> InferenceOption: ...
    
    @Occurrence.setter
    def Occurrence(self, value: InferenceOption) -> None: ...
    
    @property
    def TypeInference(self) -> InferenceOption: ...
    
    @TypeInference.setter
    def TypeInference(self, value: InferenceOption) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def InferSchema(self, instanceDocument: XmlReader) -> XmlSchemaSet: ...
    
    @overload
    def InferSchema(self, instanceDocument: XmlReader, schemas: XmlSchemaSet) -> XmlSchemaSet: ...
    
    def get_Occurrence(self) -> InferenceOption: ...
    
    def get_TypeInference(self) -> InferenceOption: ...
    
    def set_Occurrence(self, value: InferenceOption) -> VoidType: ...
    
    def set_TypeInference(self, value: InferenceOption) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class InferenceOption(Enum):
        Restricted: IntType = 0
        Relaxed: IntType = 1
    


class XmlSchemaInferenceException(XmlSchemaException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception, lineNumber: IntType, linePosition: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaInfo(ObjectType, IXmlSchemaInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContentType(self) -> XmlSchemaContentType: ...
    
    @ContentType.setter
    def ContentType(self, value: XmlSchemaContentType) -> None: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @IsDefault.setter
    def IsDefault(self, value: BooleanType) -> None: ...
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    @IsNil.setter
    def IsNil(self, value: BooleanType) -> None: ...
    
    @property
    def MemberType(self) -> XmlSchemaSimpleType: ...
    
    @MemberType.setter
    def MemberType(self, value: XmlSchemaSimpleType) -> None: ...
    
    @property
    def SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    @SchemaAttribute.setter
    def SchemaAttribute(self, value: XmlSchemaAttribute) -> None: ...
    
    @property
    def SchemaElement(self) -> XmlSchemaElement: ...
    
    @SchemaElement.setter
    def SchemaElement(self, value: XmlSchemaElement) -> None: ...
    
    @property
    def SchemaType(self) -> XmlSchemaType: ...
    
    @SchemaType.setter
    def SchemaType(self, value: XmlSchemaType) -> None: ...
    
    @property
    def Validity(self) -> XmlSchemaValidity: ...
    
    @Validity.setter
    def Validity(self, value: XmlSchemaValidity) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ContentType(self) -> XmlSchemaContentType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    def get_MemberType(self) -> XmlSchemaSimpleType: ...
    
    def get_SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    def get_SchemaElement(self) -> XmlSchemaElement: ...
    
    def get_SchemaType(self) -> XmlSchemaType: ...
    
    def get_Validity(self) -> XmlSchemaValidity: ...
    
    def set_ContentType(self, value: XmlSchemaContentType) -> VoidType: ...
    
    def set_IsDefault(self, value: BooleanType) -> VoidType: ...
    
    def set_IsNil(self, value: BooleanType) -> VoidType: ...
    
    def set_MemberType(self, value: XmlSchemaSimpleType) -> VoidType: ...
    
    def set_SchemaAttribute(self, value: XmlSchemaAttribute) -> VoidType: ...
    
    def set_SchemaElement(self, value: XmlSchemaElement) -> VoidType: ...
    
    def set_SchemaType(self, value: XmlSchemaType) -> VoidType: ...
    
    def set_Validity(self, value: XmlSchemaValidity) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaKey(XmlSchemaIdentityConstraint):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaKeyref(XmlSchemaIdentityConstraint):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Refer(self) -> XmlQualifiedName: ...
    
    @Refer.setter
    def Refer(self, value: XmlQualifiedName) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Refer(self) -> XmlQualifiedName: ...
    
    def set_Refer(self, value: XmlQualifiedName) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaLengthFacet(XmlSchemaNumericFacet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaMaxExclusiveFacet(XmlSchemaFacet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaMaxInclusiveFacet(XmlSchemaFacet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaMaxLengthFacet(XmlSchemaNumericFacet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaMinExclusiveFacet(XmlSchemaFacet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaMinInclusiveFacet(XmlSchemaFacet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaMinLengthFacet(XmlSchemaNumericFacet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaNotation(XmlSchemaAnnotated):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Public(self) -> StringType: ...
    
    @Public.setter
    def Public(self, value: StringType) -> None: ...
    
    @property
    def System(self) -> StringType: ...
    
    @System.setter
    def System(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_Public(self) -> StringType: ...
    
    def get_System(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Public(self, value: StringType) -> VoidType: ...
    
    def set_System(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaNumericFacet(ABC, XmlSchemaFacet):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaObject(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @LineNumber.setter
    def LineNumber(self, value: IntType) -> None: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @LinePosition.setter
    def LinePosition(self, value: IntType) -> None: ...
    
    @property
    def Namespaces(self) -> XmlSerializerNamespaces: ...
    
    @Namespaces.setter
    def Namespaces(self, value: XmlSerializerNamespaces) -> None: ...
    
    @property
    def Parent(self) -> XmlSchemaObject: ...
    
    @Parent.setter
    def Parent(self, value: XmlSchemaObject) -> None: ...
    
    @property
    def SourceUri(self) -> StringType: ...
    
    @SourceUri.setter
    def SourceUri(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_Namespaces(self) -> XmlSerializerNamespaces: ...
    
    def get_Parent(self) -> XmlSchemaObject: ...
    
    def get_SourceUri(self) -> StringType: ...
    
    def set_LineNumber(self, value: IntType) -> VoidType: ...
    
    def set_LinePosition(self, value: IntType) -> VoidType: ...
    
    def set_Namespaces(self, value: XmlSerializerNamespaces) -> VoidType: ...
    
    def set_Parent(self, value: XmlSchemaObject) -> VoidType: ...
    
    def set_SourceUri(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaObjectCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, parent: XmlSchemaObject): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> XmlSchemaObject: ...
    
    @Item.setter
    def Item(self, value: XmlSchemaObject) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, item: XmlSchemaObject) -> IntType: ...
    
    def Contains(self, item: XmlSchemaObject) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[XmlSchemaObject], index: IntType) -> VoidType: ...
    
    @overload
    def GetEnumerator(self) -> XmlSchemaObjectEnumerator: ...
    
    def IndexOf(self, item: XmlSchemaObject) -> IntType: ...
    
    def Insert(self, index: IntType, item: XmlSchemaObject) -> VoidType: ...
    
    def Remove(self, item: XmlSchemaObject) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> XmlSchemaObject: ...
    
    def set_Item(self, index: IntType, value: XmlSchemaObject) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaObjectEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XmlSchemaObject: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> XmlSchemaObject: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaObjectTable(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> XmlSchemaObject: ...
    
    @property
    def Names(self) -> ICollection: ...
    
    @property
    def Values(self) -> ICollection: ...
    
    # ---------- Methods ---------- #
    
    def Contains(self, name: XmlQualifiedName) -> BooleanType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, name: XmlQualifiedName) -> XmlSchemaObject: ...
    
    def get_Names(self) -> ICollection: ...
    
    def get_Values(self) -> ICollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaParticle(ABC, XmlSchemaAnnotated):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def MaxOccurs(self) -> DecimalType: ...
    
    @MaxOccurs.setter
    def MaxOccurs(self, value: DecimalType) -> None: ...
    
    @property
    def MaxOccursString(self) -> StringType: ...
    
    @MaxOccursString.setter
    def MaxOccursString(self, value: StringType) -> None: ...
    
    @property
    def MinOccurs(self) -> DecimalType: ...
    
    @MinOccurs.setter
    def MinOccurs(self, value: DecimalType) -> None: ...
    
    @property
    def MinOccursString(self) -> StringType: ...
    
    @MinOccursString.setter
    def MinOccursString(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_MaxOccurs(self) -> DecimalType: ...
    
    def get_MaxOccursString(self) -> StringType: ...
    
    def get_MinOccurs(self) -> DecimalType: ...
    
    def get_MinOccursString(self) -> StringType: ...
    
    def set_MaxOccurs(self, value: DecimalType) -> VoidType: ...
    
    def set_MaxOccursString(self, value: StringType) -> VoidType: ...
    
    def set_MinOccurs(self, value: DecimalType) -> VoidType: ...
    
    def set_MinOccursString(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaPatternFacet(XmlSchemaFacet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaRedefine(XmlSchemaExternal):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeGroups(self) -> XmlSchemaObjectTable: ...
    
    @property
    def Groups(self) -> XmlSchemaObjectTable: ...
    
    @property
    def Items(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def SchemaTypes(self) -> XmlSchemaObjectTable: ...
    
    # ---------- Methods ---------- #
    
    def get_AttributeGroups(self) -> XmlSchemaObjectTable: ...
    
    def get_Groups(self) -> XmlSchemaObjectTable: ...
    
    def get_Items(self) -> XmlSchemaObjectCollection: ...
    
    def get_SchemaTypes(self) -> XmlSchemaObjectTable: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaSequence(XmlSchemaGroupBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Items(self) -> XmlSchemaObjectCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Items(self) -> XmlSchemaObjectCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaSet(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, nameTable: XmlNameTable): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CompilationSettings(self) -> XmlSchemaCompilationSettings: ...
    
    @CompilationSettings.setter
    def CompilationSettings(self, value: XmlSchemaCompilationSettings) -> None: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def GlobalAttributes(self) -> XmlSchemaObjectTable: ...
    
    @property
    def GlobalElements(self) -> XmlSchemaObjectTable: ...
    
    @property
    def GlobalTypes(self) -> XmlSchemaObjectTable: ...
    
    @property
    def IsCompiled(self) -> BooleanType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, targetNamespace: StringType, schemaUri: StringType) -> XmlSchema: ...
    
    @overload
    def Add(self, targetNamespace: StringType, schemaDocument: XmlReader) -> XmlSchema: ...
    
    @overload
    def Add(self, schemas: XmlSchemaSet) -> VoidType: ...
    
    @overload
    def Add(self, schema: XmlSchema) -> XmlSchema: ...
    
    def Compile(self) -> VoidType: ...
    
    @overload
    def Contains(self, targetNamespace: StringType) -> BooleanType: ...
    
    @overload
    def Contains(self, schema: XmlSchema) -> BooleanType: ...
    
    def CopyTo(self, schemas: ArrayType[XmlSchema], index: IntType) -> VoidType: ...
    
    def Remove(self, schema: XmlSchema) -> XmlSchema: ...
    
    def RemoveRecursive(self, schemaToRemove: XmlSchema) -> BooleanType: ...
    
    def Reprocess(self, schema: XmlSchema) -> XmlSchema: ...
    
    @overload
    def Schemas(self) -> ICollection: ...
    
    @overload
    def Schemas(self, targetNamespace: StringType) -> ICollection: ...
    
    def add_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def get_CompilationSettings(self) -> XmlSchemaCompilationSettings: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_GlobalAttributes(self) -> XmlSchemaObjectTable: ...
    
    def get_GlobalElements(self) -> XmlSchemaObjectTable: ...
    
    def get_GlobalTypes(self) -> XmlSchemaObjectTable: ...
    
    def get_IsCompiled(self) -> BooleanType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def remove_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def set_CompilationSettings(self, value: XmlSchemaCompilationSettings) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ValidationEventHandler: EventType[ValidationEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaSimpleContent(XmlSchemaContentModel):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Content(self) -> XmlSchemaContent: ...
    
    @Content.setter
    def Content(self, value: XmlSchemaContent) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Content(self) -> XmlSchemaContent: ...
    
    def set_Content(self, value: XmlSchemaContent) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaSimpleContentExtension(XmlSchemaContent):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AnyAttribute(self) -> XmlSchemaAnyAttribute: ...
    
    @AnyAttribute.setter
    def AnyAttribute(self, value: XmlSchemaAnyAttribute) -> None: ...
    
    @property
    def Attributes(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def BaseTypeName(self) -> XmlQualifiedName: ...
    
    @BaseTypeName.setter
    def BaseTypeName(self, value: XmlQualifiedName) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AnyAttribute(self) -> XmlSchemaAnyAttribute: ...
    
    def get_Attributes(self) -> XmlSchemaObjectCollection: ...
    
    def get_BaseTypeName(self) -> XmlQualifiedName: ...
    
    def set_AnyAttribute(self, value: XmlSchemaAnyAttribute) -> VoidType: ...
    
    def set_BaseTypeName(self, value: XmlQualifiedName) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaSimpleContentRestriction(XmlSchemaContent):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AnyAttribute(self) -> XmlSchemaAnyAttribute: ...
    
    @AnyAttribute.setter
    def AnyAttribute(self, value: XmlSchemaAnyAttribute) -> None: ...
    
    @property
    def Attributes(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def BaseType(self) -> XmlSchemaSimpleType: ...
    
    @BaseType.setter
    def BaseType(self, value: XmlSchemaSimpleType) -> None: ...
    
    @property
    def BaseTypeName(self) -> XmlQualifiedName: ...
    
    @BaseTypeName.setter
    def BaseTypeName(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def Facets(self) -> XmlSchemaObjectCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_AnyAttribute(self) -> XmlSchemaAnyAttribute: ...
    
    def get_Attributes(self) -> XmlSchemaObjectCollection: ...
    
    def get_BaseType(self) -> XmlSchemaSimpleType: ...
    
    def get_BaseTypeName(self) -> XmlQualifiedName: ...
    
    def get_Facets(self) -> XmlSchemaObjectCollection: ...
    
    def set_AnyAttribute(self, value: XmlSchemaAnyAttribute) -> VoidType: ...
    
    def set_BaseType(self, value: XmlSchemaSimpleType) -> VoidType: ...
    
    def set_BaseTypeName(self, value: XmlQualifiedName) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaSimpleType(XmlSchemaType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Content(self) -> XmlSchemaSimpleTypeContent: ...
    
    @Content.setter
    def Content(self, value: XmlSchemaSimpleTypeContent) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Content(self) -> XmlSchemaSimpleTypeContent: ...
    
    def set_Content(self, value: XmlSchemaSimpleTypeContent) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaSimpleTypeContent(ABC, XmlSchemaAnnotated):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaSimpleTypeList(XmlSchemaSimpleTypeContent):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseItemType(self) -> XmlSchemaSimpleType: ...
    
    @BaseItemType.setter
    def BaseItemType(self, value: XmlSchemaSimpleType) -> None: ...
    
    @property
    def ItemType(self) -> XmlSchemaSimpleType: ...
    
    @ItemType.setter
    def ItemType(self, value: XmlSchemaSimpleType) -> None: ...
    
    @property
    def ItemTypeName(self) -> XmlQualifiedName: ...
    
    @ItemTypeName.setter
    def ItemTypeName(self, value: XmlQualifiedName) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_BaseItemType(self) -> XmlSchemaSimpleType: ...
    
    def get_ItemType(self) -> XmlSchemaSimpleType: ...
    
    def get_ItemTypeName(self) -> XmlQualifiedName: ...
    
    def set_BaseItemType(self, value: XmlSchemaSimpleType) -> VoidType: ...
    
    def set_ItemType(self, value: XmlSchemaSimpleType) -> VoidType: ...
    
    def set_ItemTypeName(self, value: XmlQualifiedName) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaSimpleTypeRestriction(XmlSchemaSimpleTypeContent):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseType(self) -> XmlSchemaSimpleType: ...
    
    @BaseType.setter
    def BaseType(self, value: XmlSchemaSimpleType) -> None: ...
    
    @property
    def BaseTypeName(self) -> XmlQualifiedName: ...
    
    @BaseTypeName.setter
    def BaseTypeName(self, value: XmlQualifiedName) -> None: ...
    
    @property
    def Facets(self) -> XmlSchemaObjectCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_BaseType(self) -> XmlSchemaSimpleType: ...
    
    def get_BaseTypeName(self) -> XmlQualifiedName: ...
    
    def get_Facets(self) -> XmlSchemaObjectCollection: ...
    
    def set_BaseType(self, value: XmlSchemaSimpleType) -> VoidType: ...
    
    def set_BaseTypeName(self, value: XmlQualifiedName) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaSimpleTypeUnion(XmlSchemaSimpleTypeContent):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseMemberTypes(self) -> ArrayType[XmlSchemaSimpleType]: ...
    
    @property
    def BaseTypes(self) -> XmlSchemaObjectCollection: ...
    
    @property
    def MemberTypes(self) -> ArrayType[XmlQualifiedName]: ...
    
    @MemberTypes.setter
    def MemberTypes(self, value: ArrayType[XmlQualifiedName]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_BaseMemberTypes(self) -> ArrayType[XmlSchemaSimpleType]: ...
    
    def get_BaseTypes(self) -> XmlSchemaObjectCollection: ...
    
    def get_MemberTypes(self) -> ArrayType[XmlQualifiedName]: ...
    
    def set_MemberTypes(self, value: ArrayType[XmlQualifiedName]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaSubstitutionGroup(XmlSchemaObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaSubstitutionGroupV1Compat(XmlSchemaSubstitutionGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaTotalDigitsFacet(XmlSchemaNumericFacet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaType(XmlSchemaAnnotated):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseSchemaType(self) -> ObjectType: ...
    
    @property
    def BaseXmlSchemaType(self) -> XmlSchemaType: ...
    
    @property
    def Datatype(self) -> XmlSchemaDatatype: ...
    
    @property
    def DerivedBy(self) -> XmlSchemaDerivationMethod: ...
    
    @property
    def Final(self) -> XmlSchemaDerivationMethod: ...
    
    @Final.setter
    def Final(self, value: XmlSchemaDerivationMethod) -> None: ...
    
    @property
    def FinalResolved(self) -> XmlSchemaDerivationMethod: ...
    
    @property
    def IsMixed(self) -> BooleanType: ...
    
    @IsMixed.setter
    def IsMixed(self, value: BooleanType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def QualifiedName(self) -> XmlQualifiedName: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def GetBuiltInComplexType(typeCode: XmlTypeCode) -> XmlSchemaComplexType: ...
    
    @staticmethod
    @overload
    def GetBuiltInComplexType(qualifiedName: XmlQualifiedName) -> XmlSchemaComplexType: ...
    
    @staticmethod
    @overload
    def GetBuiltInSimpleType(qualifiedName: XmlQualifiedName) -> XmlSchemaSimpleType: ...
    
    @staticmethod
    @overload
    def GetBuiltInSimpleType(typeCode: XmlTypeCode) -> XmlSchemaSimpleType: ...
    
    @staticmethod
    def IsDerivedFrom(derivedType: XmlSchemaType, baseType: XmlSchemaType, _except: XmlSchemaDerivationMethod) -> BooleanType: ...
    
    def get_BaseSchemaType(self) -> ObjectType: ...
    
    def get_BaseXmlSchemaType(self) -> XmlSchemaType: ...
    
    def get_Datatype(self) -> XmlSchemaDatatype: ...
    
    def get_DerivedBy(self) -> XmlSchemaDerivationMethod: ...
    
    def get_Final(self) -> XmlSchemaDerivationMethod: ...
    
    def get_FinalResolved(self) -> XmlSchemaDerivationMethod: ...
    
    def get_IsMixed(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_QualifiedName(self) -> XmlQualifiedName: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def set_Final(self, value: XmlSchemaDerivationMethod) -> VoidType: ...
    
    def set_IsMixed(self, value: BooleanType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaUnique(XmlSchemaIdentityConstraint):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaValidationException(XmlSchemaException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception, lineNumber: IntType, linePosition: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SourceObject(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_SourceObject(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaValidator(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, nameTable: XmlNameTable, schemas: XmlSchemaSet, namespaceResolver: IXmlNamespaceResolver, validationFlags: XmlSchemaValidationFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def LineInfoProvider(self) -> IXmlLineInfo: ...
    
    @LineInfoProvider.setter
    def LineInfoProvider(self, value: IXmlLineInfo) -> None: ...
    
    @property
    def SourceUri(self) -> Uri: ...
    
    @SourceUri.setter
    def SourceUri(self, value: Uri) -> None: ...
    
    @property
    def ValidationEventSender(self) -> ObjectType: ...
    
    @ValidationEventSender.setter
    def ValidationEventSender(self, value: ObjectType) -> None: ...
    
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddSchema(self, schema: XmlSchema) -> VoidType: ...
    
    def EndValidation(self) -> VoidType: ...
    
    def GetExpectedAttributes(self) -> ArrayType[XmlSchemaAttribute]: ...
    
    def GetExpectedParticles(self) -> ArrayType[XmlSchemaParticle]: ...
    
    def GetUnspecifiedDefaultAttributes(self, defaultAttributes: ArrayList) -> VoidType: ...
    
    @overload
    def Initialize(self) -> VoidType: ...
    
    @overload
    def Initialize(self, partialValidationType: XmlSchemaObject) -> VoidType: ...
    
    def SkipToEndElement(self, schemaInfo: XmlSchemaInfo) -> VoidType: ...
    
    @overload
    def ValidateAttribute(self, localName: StringType, namespaceUri: StringType, attributeValue: StringType, schemaInfo: XmlSchemaInfo) -> ObjectType: ...
    
    @overload
    def ValidateAttribute(self, localName: StringType, namespaceUri: StringType, attributeValue: XmlValueGetter, schemaInfo: XmlSchemaInfo) -> ObjectType: ...
    
    @overload
    def ValidateElement(self, localName: StringType, namespaceUri: StringType, schemaInfo: XmlSchemaInfo) -> VoidType: ...
    
    @overload
    def ValidateElement(self, localName: StringType, namespaceUri: StringType, schemaInfo: XmlSchemaInfo, xsiType: StringType, xsiNil: StringType, xsiSchemaLocation: StringType, xsiNoNamespaceSchemaLocation: StringType) -> VoidType: ...
    
    @overload
    def ValidateEndElement(self, schemaInfo: XmlSchemaInfo) -> ObjectType: ...
    
    @overload
    def ValidateEndElement(self, schemaInfo: XmlSchemaInfo, typedValue: ObjectType) -> ObjectType: ...
    
    def ValidateEndOfAttributes(self, schemaInfo: XmlSchemaInfo) -> VoidType: ...
    
    @overload
    def ValidateText(self, elementValue: StringType) -> VoidType: ...
    
    @overload
    def ValidateText(self, elementValue: XmlValueGetter) -> VoidType: ...
    
    @overload
    def ValidateWhitespace(self, elementValue: StringType) -> VoidType: ...
    
    @overload
    def ValidateWhitespace(self, elementValue: XmlValueGetter) -> VoidType: ...
    
    def add_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def get_LineInfoProvider(self) -> IXmlLineInfo: ...
    
    def get_SourceUri(self) -> Uri: ...
    
    def get_ValidationEventSender(self) -> ObjectType: ...
    
    def remove_ValidationEventHandler(self, value: ValidationEventHandler) -> VoidType: ...
    
    def set_LineInfoProvider(self, value: IXmlLineInfo) -> VoidType: ...
    
    def set_SourceUri(self, value: Uri) -> VoidType: ...
    
    def set_ValidationEventSender(self, value: ObjectType) -> VoidType: ...
    
    def set_XmlResolver(self, value: XmlResolver) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ValidationEventHandler: EventType[ValidationEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaWhiteSpaceFacet(XmlSchemaFacet):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaXPath(XmlSchemaAnnotated):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def XPath(self) -> StringType: ...
    
    @XPath.setter
    def XPath(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_XPath(self) -> StringType: ...
    
    def set_XPath(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlStringConverter(XmlBaseConverter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: StringType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @staticmethod
    def Create(schemaType: XmlSchemaType) -> XmlValueConverter: ...
    
    @overload
    def ToString(self, value: StringType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    @overload
    def ToString(self, value: ObjectType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlUnionConverter(XmlBaseConverter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @staticmethod
    def Create(schemaType: XmlSchemaType) -> XmlValueConverter: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlUntypedConverter(XmlListConverter):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Untyped() -> XmlValueConverter: ...
    
    @staticmethod
    @property
    def UntypedList() -> XmlValueConverter: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: DateTime, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DateTimeOffset, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DecimalType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DoubleType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: IntType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: LongType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: FloatType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: StringType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: BooleanType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ToBoolean(self, value: StringType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, value: StringType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: ObjectType) -> DateTime: ...
    
    @overload
    def ToDateTimeOffset(self, value: StringType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: ObjectType) -> DateTimeOffset: ...
    
    @overload
    def ToDecimal(self, value: StringType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: ObjectType) -> DecimalType: ...
    
    @overload
    def ToDouble(self, value: StringType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: ObjectType) -> DoubleType: ...
    
    @overload
    def ToInt32(self, value: StringType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: ObjectType) -> IntType: ...
    
    @overload
    def ToInt64(self, value: StringType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: ObjectType) -> LongType: ...
    
    @overload
    def ToSingle(self, value: StringType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: ObjectType) -> FloatType: ...
    
    @overload
    def ToString(self, value: DateTime) -> StringType: ...
    
    @overload
    def ToString(self, value: DateTimeOffset) -> StringType: ...
    
    @overload
    def ToString(self, value: DecimalType) -> StringType: ...
    
    @overload
    def ToString(self, value: DoubleType) -> StringType: ...
    
    @overload
    def ToString(self, value: IntType) -> StringType: ...
    
    @overload
    def ToString(self, value: LongType) -> StringType: ...
    
    @overload
    def ToString(self, value: FloatType) -> StringType: ...
    
    @overload
    def ToString(self, value: StringType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    @overload
    def ToString(self, value: BooleanType) -> StringType: ...
    
    @overload
    def ToString(self, value: ObjectType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlValueConverter(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ChangeType(self, value: BooleanType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: IntType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: LongType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DecimalType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: FloatType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DoubleType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DateTime, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: DateTimeOffset, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: StringType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: StringType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def ChangeType(self, value: ObjectType, destinationType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ToBoolean(self, value: BooleanType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: LongType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: IntType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: DecimalType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: FloatType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: DoubleType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: DateTime) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: DateTimeOffset) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: StringType) -> BooleanType: ...
    
    @overload
    def ToBoolean(self, value: ObjectType) -> BooleanType: ...
    
    @overload
    def ToDateTime(self, value: BooleanType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: IntType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: LongType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: DecimalType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: FloatType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: DoubleType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: DateTime) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: DateTimeOffset) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: StringType) -> DateTime: ...
    
    @overload
    def ToDateTime(self, value: ObjectType) -> DateTime: ...
    
    @overload
    def ToDateTimeOffset(self, value: BooleanType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: IntType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: LongType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: DecimalType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: FloatType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: DoubleType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: DateTime) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: DateTimeOffset) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: StringType) -> DateTimeOffset: ...
    
    @overload
    def ToDateTimeOffset(self, value: ObjectType) -> DateTimeOffset: ...
    
    @overload
    def ToDecimal(self, value: BooleanType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: IntType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: LongType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: DecimalType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: FloatType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: DoubleType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: DateTime) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: DateTimeOffset) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: StringType) -> DecimalType: ...
    
    @overload
    def ToDecimal(self, value: ObjectType) -> DecimalType: ...
    
    @overload
    def ToDouble(self, value: BooleanType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: IntType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: LongType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: DecimalType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: FloatType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: DoubleType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: DateTime) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: DateTimeOffset) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: StringType) -> DoubleType: ...
    
    @overload
    def ToDouble(self, value: ObjectType) -> DoubleType: ...
    
    @overload
    def ToInt32(self, value: BooleanType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: IntType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: LongType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: DecimalType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: FloatType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: DoubleType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: DateTime) -> IntType: ...
    
    @overload
    def ToInt32(self, value: DateTimeOffset) -> IntType: ...
    
    @overload
    def ToInt32(self, value: StringType) -> IntType: ...
    
    @overload
    def ToInt32(self, value: ObjectType) -> IntType: ...
    
    @overload
    def ToInt64(self, value: BooleanType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: IntType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: LongType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: DecimalType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: FloatType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: DoubleType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: DateTime) -> LongType: ...
    
    @overload
    def ToInt64(self, value: DateTimeOffset) -> LongType: ...
    
    @overload
    def ToInt64(self, value: StringType) -> LongType: ...
    
    @overload
    def ToInt64(self, value: ObjectType) -> LongType: ...
    
    @overload
    def ToSingle(self, value: BooleanType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: IntType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: LongType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: DecimalType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: FloatType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: DoubleType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: DateTime) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: DateTimeOffset) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: StringType) -> FloatType: ...
    
    @overload
    def ToSingle(self, value: ObjectType) -> FloatType: ...
    
    @overload
    def ToString(self, value: BooleanType) -> StringType: ...
    
    @overload
    def ToString(self, value: IntType) -> StringType: ...
    
    @overload
    def ToString(self, value: LongType) -> StringType: ...
    
    @overload
    def ToString(self, value: DecimalType) -> StringType: ...
    
    @overload
    def ToString(self, value: FloatType) -> StringType: ...
    
    @overload
    def ToString(self, value: DoubleType) -> StringType: ...
    
    @overload
    def ToString(self, value: DateTime) -> StringType: ...
    
    @overload
    def ToString(self, value: DateTimeOffset) -> StringType: ...
    
    @overload
    def ToString(self, value: StringType) -> StringType: ...
    
    @overload
    def ToString(self, value: StringType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    @overload
    def ToString(self, value: ObjectType) -> StringType: ...
    
    @overload
    def ToString(self, value: ObjectType, nsResolver: IXmlNamespaceResolver) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlValueGetter(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> ObjectType: ...
    
    def Invoke(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsdBuilder(SchemaBuilder):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsdSimpleValue(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, st: XmlSchemaSimpleType, value: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypedValue(self) -> ObjectType: ...
    
    @property
    def XmlType(self) -> XmlSchemaSimpleType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypedValue(self) -> ObjectType: ...
    
    def get_XmlType(self) -> XmlSchemaSimpleType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsdValidator(BaseValidator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @Context.setter
    def Context(self, value: ValidationState) -> None: ...
    
    @staticmethod
    @property
    def DtQName() -> XmlSchemaDatatype: ...
    
    @property
    def PreserveWhitespace(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def CompleteValidation(self) -> VoidType: ...
    
    def FindId(self, name: StringType) -> ObjectType: ...
    
    def IsXSDRoot(self, localName: StringType, ns: StringType) -> BooleanType: ...
    
    def Validate(self) -> VoidType: ...
    
    @staticmethod
    def get_DtQName() -> XmlSchemaDatatype: ...
    
    def get_PreserveWhitespace(self) -> BooleanType: ...
    
    def set_Context(self, value: ValidationState) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class Position(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def particle(self) -> ObjectType: ...
    
    @particle.setter
    def particle(self, value: ObjectType) -> None: ...
    
    @property
    def symbol(self) -> IntType: ...
    
    @symbol.setter
    def symbol(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, symbol: IntType, particle: ObjectType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RangePositionInfo(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def curpos(self) -> BitSet: ...
    
    @curpos.setter
    def curpos(self, value: BitSet) -> None: ...
    
    @property
    def rangeCounters(self) -> ArrayType[DecimalType]: ...
    
    @rangeCounters.setter
    def rangeCounters(self, value: ArrayType[DecimalType]) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StateUnion(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def AllElementsRequired(self) -> IntType: ...
    
    @AllElementsRequired.setter
    def AllElementsRequired(self, value: IntType) -> None: ...
    
    @property
    def CurPosIndex(self) -> IntType: ...
    
    @CurPosIndex.setter
    def CurPosIndex(self, value: IntType) -> None: ...
    
    @property
    def NumberOfRunningPos(self) -> IntType: ...
    
    @NumberOfRunningPos.setter
    def NumberOfRunningPos(self, value: IntType) -> None: ...
    
    @property
    def State(self) -> IntType: ...
    
    @State.setter
    def State(self, value: IntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsdDateTime(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, text: StringType): ...
    
    @overload
    def __init__(self, text: StringType, kinds: XsdDateTimeFlags): ...
    
    @overload
    def __init__(self, dateTime: DateTime, kinds: XsdDateTimeFlags): ...
    
    @overload
    def __init__(self, dateTimeOffset: DateTimeOffset): ...
    
    @overload
    def __init__(self, dateTimeOffset: DateTimeOffset, kinds: XsdDateTimeFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Day(self) -> IntType: ...
    
    @property
    def Fraction(self) -> IntType: ...
    
    @property
    def Hour(self) -> IntType: ...
    
    @property
    def Kind(self) -> DateTimeKind: ...
    
    @property
    def Minute(self) -> IntType: ...
    
    @property
    def Month(self) -> IntType: ...
    
    @property
    def Second(self) -> IntType: ...
    
    @property
    def TypeCode(self) -> XmlTypeCode: ...
    
    @property
    def Year(self) -> IntType: ...
    
    @property
    def ZoneHour(self) -> IntType: ...
    
    @property
    def ZoneMinute(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Compare(left: XsdDateTime, right: XsdDateTime) -> IntType: ...
    
    def CompareTo(self, value: ObjectType) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def ToZulu(self) -> DateTime: ...
    
    def get_Day(self) -> IntType: ...
    
    def get_Fraction(self) -> IntType: ...
    
    def get_Hour(self) -> IntType: ...
    
    def get_Kind(self) -> DateTimeKind: ...
    
    def get_Minute(self) -> IntType: ...
    
    def get_Month(self) -> IntType: ...
    
    def get_Second(self) -> IntType: ...
    
    def get_TypeCode(self) -> XmlTypeCode: ...
    
    def get_Year(self) -> IntType: ...
    
    def get_ZoneHour(self) -> IntType: ...
    
    def get_ZoneMinute(self) -> IntType: ...
    
    @staticmethod
    @overload
    def op_Implicit(xdt: XsdDateTime) -> DateTime: ...
    
    @staticmethod
    @overload
    def op_Implicit(xdt: XsdDateTime) -> DateTimeOffset: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XsdDuration(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, isNegative: BooleanType, years: IntType, months: IntType, days: IntType, hours: IntType, minutes: IntType, seconds: IntType, nanoseconds: IntType): ...
    
    @overload
    def __init__(self, timeSpan: TimeSpan): ...
    
    @overload
    def __init__(self, timeSpan: TimeSpan, durationType: DurationType): ...
    
    @overload
    def __init__(self, s: StringType): ...
    
    @overload
    def __init__(self, s: StringType, durationType: DurationType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Days(self) -> IntType: ...
    
    @property
    def Hours(self) -> IntType: ...
    
    @property
    def IsNegative(self) -> BooleanType: ...
    
    @property
    def Microseconds(self) -> IntType: ...
    
    @property
    def Milliseconds(self) -> IntType: ...
    
    @property
    def Minutes(self) -> IntType: ...
    
    @property
    def Months(self) -> IntType: ...
    
    @property
    def Nanoseconds(self) -> IntType: ...
    
    @property
    def Seconds(self) -> IntType: ...
    
    @property
    def Years(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Normalize(self) -> XsdDuration: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ToTimeSpan(self) -> TimeSpan: ...
    
    @overload
    def ToTimeSpan(self, durationType: DurationType) -> TimeSpan: ...
    
    def get_Days(self) -> IntType: ...
    
    def get_Hours(self) -> IntType: ...
    
    def get_IsNegative(self) -> BooleanType: ...
    
    def get_Microseconds(self) -> IntType: ...
    
    def get_Milliseconds(self) -> IntType: ...
    
    def get_Minutes(self) -> IntType: ...
    
    def get_Months(self) -> IntType: ...
    
    def get_Nanoseconds(self) -> IntType: ...
    
    def get_Seconds(self) -> IntType: ...
    
    def get_Years(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class DurationType(Enum):
        Duration: IntType = 0
        YearMonthDuration: IntType = 1
        DayTimeDuration: IntType = 2
    


# ---------- Interfaces ---------- #

class IXmlSchemaInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    @property
    def MemberType(self) -> XmlSchemaSimpleType: ...
    
    @property
    def SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    @property
    def SchemaElement(self) -> XmlSchemaElement: ...
    
    @property
    def SchemaType(self) -> XmlSchemaType: ...
    
    @property
    def Validity(self) -> XmlSchemaValidity: ...
    
    # ---------- Methods ---------- #
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    def get_MemberType(self) -> XmlSchemaSimpleType: ...
    
    def get_SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    def get_SchemaElement(self) -> XmlSchemaElement: ...
    
    def get_SchemaType(self) -> XmlSchemaType: ...
    
    def get_Validity(self) -> XmlSchemaValidity: ...
    
    # No Events


# ---------- Enums ---------- #

class AttributeMatchState(Enum):
    AttributeFound: IntType = 0
    AnyIdAttributeFound: IntType = 1
    UndeclaredElementAndAttribute: IntType = 2
    UndeclaredAttribute: IntType = 3
    AnyAttributeLax: IntType = 4
    AnyAttributeSkip: IntType = 5
    ProhibitedAnyAttribute: IntType = 6
    ProhibitedAttribute: IntType = 7
    AttributeNameMismatch: IntType = 8
    ValidateAttributeInvalidCall: IntType = 9


class Compositor(Enum):
    Root: IntType = 0
    Include: IntType = 1
    Import: IntType = 2
    Redefine: IntType = 3


class FacetType(Enum):
    #None: IntType = 0
    Length: IntType = 1
    MinLength: IntType = 2
    MaxLength: IntType = 3
    Pattern: IntType = 4
    Whitespace: IntType = 5
    Enumeration: IntType = 6
    MinExclusive: IntType = 7
    MinInclusive: IntType = 8
    MaxExclusive: IntType = 9
    MaxInclusive: IntType = 10
    TotalDigits: IntType = 11
    FractionDigits: IntType = 12


class RestrictionFlags(Enum):
    Length: IntType = 1
    MinLength: IntType = 2
    MaxLength: IntType = 4
    Pattern: IntType = 8
    Enumeration: IntType = 16
    WhiteSpace: IntType = 32
    MaxInclusive: IntType = 64
    MaxExclusive: IntType = 128
    MinInclusive: IntType = 256
    MinExclusive: IntType = 512
    TotalDigits: IntType = 1024
    FractionDigits: IntType = 2048


class SchemaType(Enum):
    #None: IntType = 0
    DTD: IntType = 1
    XDR: IntType = 2
    XSD: IntType = 3


class ValidatorState(Enum):
    #None: IntType = 0
    Start: IntType = 1
    TopLevelAttribute: IntType = 2
    TopLevelTextOrWS: IntType = 3
    Element: IntType = 4
    Attribute: IntType = 5
    EndOfAttributes: IntType = 6
    Text: IntType = 7
    Whitespace: IntType = 8
    EndElement: IntType = 9
    SkipToEndElement: IntType = 10
    Finish: IntType = 11


class XmlSchemaContentProcessing(Enum):
    #None: IntType = 0
    Skip: IntType = 1
    Lax: IntType = 2
    Strict: IntType = 3


class XmlSchemaContentType(Enum):
    TextOnly: IntType = 0
    Empty: IntType = 1
    ElementOnly: IntType = 2
    Mixed: IntType = 3


class XmlSchemaDatatypeVariety(Enum):
    Atomic: IntType = 0
    List: IntType = 1
    Union: IntType = 2


class XmlSchemaDerivationMethod(Enum):
    Empty: IntType = 0
    Substitution: IntType = 1
    Extension: IntType = 2
    Restriction: IntType = 4
    List: IntType = 8
    Union: IntType = 16
    All: IntType = 255
    #None: IntType = 256


class XmlSchemaForm(Enum):
    #None: IntType = 0
    Qualified: IntType = 1
    Unqualified: IntType = 2


class XmlSchemaUse(Enum):
    #None: IntType = 0
    Optional: IntType = 1
    Prohibited: IntType = 2
    Required: IntType = 3


class XmlSchemaValidationFlags(Enum):
    #None: IntType = 0
    ProcessInlineSchema: IntType = 1
    ProcessSchemaLocation: IntType = 2
    ReportValidationWarnings: IntType = 4
    ProcessIdentityConstraints: IntType = 8
    AllowXmlAttributes: IntType = 16


class XmlSchemaValidity(Enum):
    NotKnown: IntType = 0
    Valid: IntType = 1
    Invalid: IntType = 2


class XmlSchemaWhiteSpace(Enum):
    Preserve: IntType = 0
    Replace: IntType = 1
    Collapse: IntType = 2


class XmlSeverityType(Enum):
    Error: IntType = 0
    Warning: IntType = 1


class XmlTypeCode(Enum):
    #None: IntType = 0
    Item: IntType = 1
    Node: IntType = 2
    Document: IntType = 3
    Element: IntType = 4
    Attribute: IntType = 5
    Namespace: IntType = 6
    ProcessingInstruction: IntType = 7
    Comment: IntType = 8
    Text: IntType = 9
    AnyAtomicType: IntType = 10
    UntypedAtomic: IntType = 11
    String: IntType = 12
    Boolean: IntType = 13
    Decimal: IntType = 14
    Float: IntType = 15
    Double: IntType = 16
    Duration: IntType = 17
    DateTime: IntType = 18
    Time: IntType = 19
    Date: IntType = 20
    GYearMonth: IntType = 21
    GYear: IntType = 22
    GMonthDay: IntType = 23
    GDay: IntType = 24
    GMonth: IntType = 25
    HexBinary: IntType = 26
    Base64Binary: IntType = 27
    AnyUri: IntType = 28
    QName: IntType = 29
    Notation: IntType = 30
    NormalizedString: IntType = 31
    Token: IntType = 32
    Language: IntType = 33
    NmToken: IntType = 34
    Name: IntType = 35
    NCName: IntType = 36
    Id: IntType = 37
    Idref: IntType = 38
    Entity: IntType = 39
    Integer: IntType = 40
    NonPositiveInteger: IntType = 41
    NegativeInteger: IntType = 42
    Long: IntType = 43
    Int: IntType = 44
    Short: IntType = 45
    Byte: IntType = 46
    NonNegativeInteger: IntType = 47
    UnsignedLong: IntType = 48
    UnsignedInt: IntType = 49
    UnsignedShort: IntType = 50
    UnsignedByte: IntType = 51
    PositiveInteger: IntType = 52
    YearMonthDuration: IntType = 53
    DayTimeDuration: IntType = 54


class XsdDateTimeFlags(Enum):
    DateTime: IntType = 1
    Time: IntType = 2
    Date: IntType = 4
    GYearMonth: IntType = 8
    GYear: IntType = 16
    GMonthDay: IntType = 32
    GDay: IntType = 64
    GMonth: IntType = 128
    AllXsd: IntType = 255
    XdrDateTimeNoTz: IntType = 256
    XdrDateTime: IntType = 512
    XdrTimeNoTz: IntType = 1024


# ---------- Delegates ---------- #

ValidationEventHandler = Callable[[ObjectType, ValidationEventArgs], VoidType]

XmlValueGetter = Callable[[], ObjectType]

__all__ = [
    ActiveAxis,
    AllElementsContentValidator,
    Asttree,
    AutoValidator,
    AxisElement,
    AxisStack,
    BaseProcessor,
    BaseValidator,
    BinaryFacetsChecker,
    BitSet,
    ChameleonKey,
    ChoiceNode,
    CompiledIdentityConstraint,
    Compiler,
    ConstraintStruct,
    ContentValidator,
    DatatypeImplementation,
    Datatype_ENTITY,
    Datatype_ENUMERATION,
    Datatype_ID,
    Datatype_IDREF,
    Datatype_List,
    Datatype_NCName,
    Datatype_NMTOKEN,
    Datatype_NOTATION,
    Datatype_Name,
    Datatype_QName,
    Datatype_QNameXdr,
    Datatype_anyAtomicType,
    Datatype_anySimpleType,
    Datatype_anyURI,
    Datatype_base64Binary,
    Datatype_boolean,
    Datatype_byte,
    Datatype_char,
    Datatype_date,
    Datatype_dateTime,
    Datatype_dateTimeBase,
    Datatype_dateTimeNoTimeZone,
    Datatype_dateTimeTimeZone,
    Datatype_day,
    Datatype_dayTimeDuration,
    Datatype_decimal,
    Datatype_double,
    Datatype_doubleXdr,
    Datatype_duration,
    Datatype_fixed,
    Datatype_float,
    Datatype_floatXdr,
    Datatype_hexBinary,
    Datatype_int,
    Datatype_integer,
    Datatype_language,
    Datatype_long,
    Datatype_month,
    Datatype_monthDay,
    Datatype_negativeInteger,
    Datatype_nonNegativeInteger,
    Datatype_nonPositiveInteger,
    Datatype_normalizedString,
    Datatype_normalizedStringV1Compat,
    Datatype_positiveInteger,
    Datatype_short,
    Datatype_string,
    Datatype_time,
    Datatype_timeNoTimeZone,
    Datatype_timeTimeZone,
    Datatype_token,
    Datatype_tokenV1Compat,
    Datatype_union,
    Datatype_unsignedByte,
    Datatype_unsignedInt,
    Datatype_unsignedLong,
    Datatype_unsignedShort,
    Datatype_untypedAtomicType,
    Datatype_uuid,
    Datatype_year,
    Datatype_yearMonth,
    Datatype_yearMonthDuration,
    DateTimeFacetsChecker,
    DfaContentValidator,
    DoubleLinkAxis,
    DtdValidator,
    DurationFacetsChecker,
    FacetsChecker,
    ForwardAxis,
    IdRefNode,
    InteriorNode,
    KSStruct,
    KeySequence,
    LeafNode,
    LeafRangeNode,
    ListFacetsChecker,
    LocatedActiveAxis,
    MiscFacetsChecker,
    NamespaceList,
    NamespaceListNode,
    NamespaceListV1Compat,
    NfaContentValidator,
    Numeric10FacetsChecker,
    Numeric2FacetsChecker,
    Parser,
    ParticleContentValidator,
    PlusNode,
    Positions,
    Preprocessor,
    QNameFacetsChecker,
    QmarkNode,
    RangeContentValidator,
    RedefineEntry,
    RestrictionFacets,
    SchemaAttDef,
    SchemaBuilder,
    SchemaCollectionCompiler,
    SchemaCollectionPreprocessor,
    SchemaDeclBase,
    SchemaElementDecl,
    SchemaEntity,
    SchemaInfo,
    SchemaNames,
    SchemaNamespaceManager,
    SchemaNotation,
    SelectorActiveAxis,
    SequenceNode,
    StarNode,
    StringFacetsChecker,
    SymbolsDictionary,
    SyntaxTreeNode,
    TypedObject,
    UnionFacetsChecker,
    UpaException,
    ValidationEventArgs,
    ValidationEventHandler,
    ValidationState,
    XdrBuilder,
    XdrValidator,
    XmlAnyConverter,
    XmlAnyListConverter,
    XmlAtomicValue,
    XmlBaseConverter,
    XmlBooleanConverter,
    XmlDateTimeConverter,
    XmlListConverter,
    XmlMiscConverter,
    XmlNodeConverter,
    XmlNumeric10Converter,
    XmlNumeric2Converter,
    XmlSchema,
    XmlSchemaAll,
    XmlSchemaAnnotated,
    XmlSchemaAnnotation,
    XmlSchemaAny,
    XmlSchemaAnyAttribute,
    XmlSchemaAppInfo,
    XmlSchemaAttribute,
    XmlSchemaAttributeGroup,
    XmlSchemaAttributeGroupRef,
    XmlSchemaChoice,
    XmlSchemaCollection,
    XmlSchemaCollectionEnumerator,
    XmlSchemaCollectionNode,
    XmlSchemaCompilationSettings,
    XmlSchemaComplexContent,
    XmlSchemaComplexContentExtension,
    XmlSchemaComplexContentRestriction,
    XmlSchemaComplexType,
    XmlSchemaContent,
    XmlSchemaContentModel,
    XmlSchemaDatatype,
    XmlSchemaDocumentation,
    XmlSchemaElement,
    XmlSchemaEnumerationFacet,
    XmlSchemaException,
    XmlSchemaExternal,
    XmlSchemaFacet,
    XmlSchemaFractionDigitsFacet,
    XmlSchemaGroup,
    XmlSchemaGroupBase,
    XmlSchemaGroupRef,
    XmlSchemaIdentityConstraint,
    XmlSchemaImport,
    XmlSchemaInclude,
    XmlSchemaInference,
    XmlSchemaInferenceException,
    XmlSchemaInfo,
    XmlSchemaKey,
    XmlSchemaKeyref,
    XmlSchemaLengthFacet,
    XmlSchemaMaxExclusiveFacet,
    XmlSchemaMaxInclusiveFacet,
    XmlSchemaMaxLengthFacet,
    XmlSchemaMinExclusiveFacet,
    XmlSchemaMinInclusiveFacet,
    XmlSchemaMinLengthFacet,
    XmlSchemaNotation,
    XmlSchemaNumericFacet,
    XmlSchemaObject,
    XmlSchemaObjectCollection,
    XmlSchemaObjectEnumerator,
    XmlSchemaObjectTable,
    XmlSchemaParticle,
    XmlSchemaPatternFacet,
    XmlSchemaRedefine,
    XmlSchemaSequence,
    XmlSchemaSet,
    XmlSchemaSimpleContent,
    XmlSchemaSimpleContentExtension,
    XmlSchemaSimpleContentRestriction,
    XmlSchemaSimpleType,
    XmlSchemaSimpleTypeContent,
    XmlSchemaSimpleTypeList,
    XmlSchemaSimpleTypeRestriction,
    XmlSchemaSimpleTypeUnion,
    XmlSchemaSubstitutionGroup,
    XmlSchemaSubstitutionGroupV1Compat,
    XmlSchemaTotalDigitsFacet,
    XmlSchemaType,
    XmlSchemaUnique,
    XmlSchemaValidationException,
    XmlSchemaValidator,
    XmlSchemaWhiteSpaceFacet,
    XmlSchemaXPath,
    XmlStringConverter,
    XmlUnionConverter,
    XmlUntypedConverter,
    XmlValueConverter,
    XmlValueGetter,
    XsdBuilder,
    XsdSimpleValue,
    XsdValidator,
    Position,
    RangePositionInfo,
    StateUnion,
    XsdDateTime,
    XsdDuration,
    IXmlSchemaInfo,
    AttributeMatchState,
    Compositor,
    FacetType,
    RestrictionFlags,
    SchemaType,
    ValidatorState,
    XmlSchemaContentProcessing,
    XmlSchemaContentType,
    XmlSchemaDatatypeVariety,
    XmlSchemaDerivationMethod,
    XmlSchemaForm,
    XmlSchemaUse,
    XmlSchemaValidationFlags,
    XmlSchemaValidity,
    XmlSchemaWhiteSpace,
    XmlSeverityType,
    XmlTypeCode,
    XsdDateTimeFlags,
    ValidationEventHandler,
    XmlValueGetter,
]