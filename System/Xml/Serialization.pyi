__all__ = [
    'CodeIdentifier',
    'CodeIdentifiers',
    'ImportContext',
    'SchemaImporter',
    'SoapAttributeAttribute',
    'SoapAttributeOverrides',
    'SoapAttributes',
    'SoapElementAttribute',
    'SoapEnumAttribute',
    'SoapIgnoreAttribute',
    'SoapIncludeAttribute',
    'SoapReflectionImporter',
    'SoapSchemaMember',
    'SoapTypeAttribute',
    'UnreferencedObjectEventArgs',
    'XmlAnyAttributeAttribute',
    'XmlAnyElementAttribute',
    'XmlAnyElementAttributes',
    'XmlArrayAttribute',
    'XmlArrayItemAttribute',
    'XmlArrayItemAttributes',
    'XmlAttributeAttribute',
    'XmlAttributeEventArgs',
    'XmlAttributeOverrides',
    'XmlAttributes',
    'XmlChoiceIdentifierAttribute',
    'XmlElementAttribute',
    'XmlElementAttributes',
    'XmlElementEventArgs',
    'XmlEnumAttribute',
    'XmlIgnoreAttribute',
    'XmlIncludeAttribute',
    'XmlMapping',
    'XmlMemberMapping',
    'XmlMembersMapping',
    'XmlNamespaceDeclarationsAttribute',
    'XmlNodeEventArgs',
    'XmlReflectionImporter',
    'XmlReflectionMember',
    'XmlRootAttribute',
    'XmlSchemaEnumerator',
    'XmlSchemaExporter',
    'XmlSchemaImporter',
    'XmlSchemaProviderAttribute',
    'XmlSchemas',
    'XmlSerializationGeneratedCode',
    'XmlSerializationReader',
    'XmlSerializationWriter',
    'XmlSerializer',
    'XmlSerializerAssemblyAttribute',
    'XmlSerializerFactory',
    'XmlSerializerImplementation',
    'XmlSerializerNamespaces',
    'XmlSerializerVersionAttribute',
    'XmlTextAttribute',
    'XmlTypeAttribute',
    'XmlTypeMapping',
    'XmlDeserializationEvents',
    'IXmlSerializable',
    'IXmlTextParser',
    'CodeGenerationOptions',
    'XmlMappingAccess',
    'UnreferencedObjectEventHandler',
    'XmlAttributeEventHandler',
    'XmlElementEventHandler',
    'XmlNodeEventHandler',
    'XmlSerializationCollectionFixupCallback',
    'XmlSerializationFixupCallback',
    'XmlSerializationReadCallback',
    'XmlSerializationWriteCallback',
]


# TODO

# ---------- CLASSES ---------- #

class CodeIdentifier:
    """Provides static methods to convert input text into names for code entities."""


class CodeIdentifiers:
    """Maintains a group of names for related code entities or type mappings that are generated by .NET's XML serialization infrastructure."""


class ImportContext:
    """Describes the context in which a set of schema is bound to .NET code entities."""


class SchemaImporter:
    """Describes a schema importer."""


class SoapAttributeAttribute:
    """Specifies that the XmlSerializer must serialize the class member as an encoded SOAP attribute."""


class SoapAttributeOverrides:
    """Allows you to override attributes applied to properties, fields, and classes when you use an XmlSerializer to serialize or deserialize an object as encoded SOAP."""


class SoapAttributes:
    """Represents a collection of attribute objects that control how the XmlSerializer serializes and deserializes SOAP methods."""


class SoapElementAttribute:
    """Specifies that the public member value be serialized by the XmlSerializer as an encoded SOAP XML element."""


class SoapEnumAttribute:
    """Controls how the XmlSerializer serializes an enumeration member."""


class SoapIgnoreAttribute:
    """Instructs the XmlSerializer not to serialize the public field or public read/write property value."""


class SoapIncludeAttribute:
    """Allows the XmlSerializer to recognize a type when it serializes or deserializes an object as encoded SOAP XML."""


class SoapReflectionImporter:
    """Generates mappings to SOAP-encoded messages from .NET types or Web service method information."""


class SoapSchemaMember:
    """Represents certain attributes of a XSD <part> element in a WSDL document for generating classes from the document."""


class SoapTypeAttribute:
    """Controls the schema generated by the XmlSerializer when a class instance is serialized as SOAP encoded XML."""


class UnreferencedObjectEventArgs:
    """Provides data for the known, but unreferenced, object found in an encoded SOAP XML stream during deserialization."""


class XmlAnyAttributeAttribute:
    """Specifies that the member (a field that returns an array of XmlAttribute objects) can contain any XML attributes."""


class XmlAnyElementAttribute:
    """Specifies that the member (a field that returns an array of XmlElement or XmlNode objects) contains objects that represent any XML element that has no corresponding member in the object being serialized or deserialized."""


class XmlAnyElementAttributes:
    """Represents a collection of XmlAnyElementAttribute objects."""


class XmlArrayAttribute:
    """Specifies that the XmlSerializer must serialize a particular class member as an array of XML elements."""


class XmlArrayItemAttribute:
    """Represents an attribute that specifies the derived types that the XmlSerializer can place in a serialized array."""


class XmlArrayItemAttributes:
    """Represents a collection of XmlArrayItemAttribute objects."""


class XmlAttributeAttribute:
    """Specifies that the XmlSerializer must serialize the class member as an XML attribute."""


class XmlAttributeEventArgs:
    """Provides data for the UnknownAttribute event."""


class XmlAttributeOverrides:
    """Allows you to override property, field, and class attributes when you use the XmlSerializer to serialize or deserialize an object."""


class XmlAttributes:
    """Represents a collection of attribute objects that control how the XmlSerializer serializes and deserializes an object."""


class XmlChoiceIdentifierAttribute:
    """Specifies that the member can be further detected by using an enumeration."""


class XmlElementAttribute:
    """Indicates that a public field or property represents an XML element when the XmlSerializer serializes or deserializes the object that contains it."""


class XmlElementAttributes:
    """Represents a collection of XmlElementAttribute objects used by the XmlSerializer to override the default way it serializes a class."""


class XmlElementEventArgs:
    """Provides data for the UnknownElement event."""


class XmlEnumAttribute:
    """Controls how the XmlSerializer serializes an enumeration member."""


class XmlIgnoreAttribute:
    """Instructs the Serialize(TextWriter, Object) method of the XmlSerializer not to serialize the public field or public read/write property value."""


class XmlIncludeAttribute:
    """Allows the XmlSerializer to recognize a type when it serializes or deserializes an object."""


class XmlMapping:
    """Supports mappings between .NET types and XML Schema data types."""


class XmlMemberMapping:
    """Maps a code entity in a .NET Web service method to an element in a Web Services Description Language (WSDL) message."""


class XmlMembersMapping:
    """Provides mappings between .NET Web service methods and Web Services Description Language (WSDL) messages that are defined for SOAP Web services."""


class XmlNamespaceDeclarationsAttribute:
    """Specifies that the target property, parameter, return value, or class member contains prefixes associated with namespaces that are used within an XML document."""


class XmlNodeEventArgs:
    """Provides data for the UnknownNode event."""


class XmlReflectionImporter:
    """Generates mappings to XML schema element declarations, including literal XML Schema Definition (XSD) message parts in a Web Services Description Language (WSDL) document, for .NET types or Web service method information."""


class XmlReflectionMember:
    """Provides mappings between code entities in .NET Web service methods and the content of Web Services Description Language (WSDL) messages that are defined for SOAP Web services."""


class XmlRootAttribute:
    """Controls XML serialization of the attribute target as an XML root element."""


class XmlSchemaEnumerator:
    """Enables iteration over a collection of XmlSchema objects."""


class XmlSchemaExporter:
    """Populates XmlSchema objects with XML schema element declarations that are found in type mapping objects."""


class XmlSchemaImporter:
    """Generates internal mappings to .NET types for XML schema element declarations, including literal XSD message parts in a WSDL document."""


class XmlSchemaProviderAttribute:
    """When applied to a type, stores the name of a static method of the type that returns an XML schema and a XmlQualifiedName (or XmlSchemaType for anonymous types) that controls the serialization of the type."""


class XmlSchemas:
    """Represents the collection of XML schemas."""


class XmlSerializationGeneratedCode:
    """An abstract class that is the base class for XmlSerializationReader and XmlSerializationWriter and that contains methods common to both of these types."""


class XmlSerializationReader:
    """Controls deserialization by the XmlSerializer class."""
    
    class CollectionFixup:
        """Holds an XmlSerializationCollectionFixupCallback delegate instance, plus the method's inputs; also supplies the method's parameters."""
    
    class Fixup:
        """Holds an XmlSerializationFixupCallback delegate instance, plus the method's inputs; also serves as the parameter for the method."""


class XmlSerializationWriter:
    """Represents an abstract class used for controlling serialization by the XmlSerializer class."""


class XmlSerializer:
    """Serializes and deserializes objects into and from XML documents. The XmlSerializer enables you to control how objects are encoded into XML."""


class XmlSerializerAssemblyAttribute:
    """Applied to a Web service client proxy, enables you to specify an assembly that contains custom-made serializers."""


class XmlSerializerFactory:
    """Creates typed versions of the XmlSerializer for more efficient serialization."""


class XmlSerializerImplementation:
    """Defines the reader, writer, and methods for pre-generated, typed serializers."""


class XmlSerializerNamespaces:
    """Contains the XML namespaces and prefixes that the XmlSerializer uses to generate qualified names in an XML-document instance."""


class XmlSerializerVersionAttribute:
    """Signifies that the code was generated by the serialization infrastructure and can be reused for increased performance, when this attribute is applied to an assembly."""


class XmlTextAttribute:
    """Indicates to the XmlSerializer that the member must be treated as XML text when the class that contains it is serialized or deserialized."""


class XmlTypeAttribute:
    """Controls the XML schema that is generated when the attribute target is serialized by the XmlSerializer."""


class XmlTypeMapping:
    """Contains a mapping of one type to another."""


# ---------- STRUCTS ---------- #

class XmlDeserializationEvents:
    """Contains fields that can be used to pass event delegates to a thread-safe Deserialize method of the XmlSerializer."""


# ---------- INTERFACES ---------- #

class IXmlSerializable:
    """Provides custom formatting for XML serialization and deserialization."""


class IXmlTextParser:
    """Establishes a Normalized property for use by the .NET infrastructure."""


# ---------- ENUMS ---------- #

class CodeGenerationOptions:
    """Specifies various options to use when generating .NET types for use with an XML Web Service."""


class XmlMappingAccess:
    """Specifies whether a mapping is read, write, or both."""


# ---------- DELEGATES ---------- #

class UnreferencedObjectEventHandler:
    """Represents the method that handles the UnreferencedObject event of an XmlSerializer."""


class XmlAttributeEventHandler:
    """Represents the method that handles the UnknownAttribute."""


class XmlElementEventHandler:
    """Represents the method that handles the UnknownElement event of an XmlSerializer."""


class XmlNodeEventHandler:
    """Represents the method that handles the UnknownNode event of an XmlSerializer."""


class XmlSerializationCollectionFixupCallback:
    """Delegate used by the XmlSerializer class for deserialization of SOAP-encoded XML data types that map to collections or enumerations."""


class XmlSerializationFixupCallback:
    """Delegate used by the XmlSerializer class for deserialization of SOAP-encoded XML data."""


class XmlSerializationReadCallback:
    """Delegate used by the XmlSerializer class for deserialization of types from SOAP-encoded, non-root XML data."""


class XmlSerializationWriteCallback:
    """Delegate that is used by the XmlSerializer class for serialization of types from SOAP-encoded, non-root XML data."""
