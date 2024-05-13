from rest_framework import serializers
from .models import Provider

class providerSerializer(serializers.ModelSerializer):
    """In Django, when you define a serializer class using Django REST Framework (DRF), you often include a nested inner class called Meta. This class allows you to specify metadata options for the serializer. Here's what it does and why it's useful:

Defining Metadata Options: The Meta class allows you to specify various metadata options for the serializer, such as the model to serialize, fields to include/exclude, and additional configuration options.

Model Association: One of the primary uses of Meta is to associate the serializer with a Django model. By setting the model attribute within the Meta class, you tell DRF which model the serializer should serialize or deserialize.

Fields Configuration: You can specify which fields from the associated model should be included or excluded in the serialized representation using the fields or exclude attribute within Meta.

Additional Configuration: Meta class can also include additional configuration options specific to how the serializer behaves, such as ordering, queryset filtering, read-only fields, and more."""
    
    class Meta:
        model=Provider
        fields='__all__'