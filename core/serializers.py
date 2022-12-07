from rest_framework.serializers import ModelSerializer

from core.models import Lista, Mercado, Produto, Usuario

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        
class MercadoSerializer(ModelSerializer):
    class Meta:
        model = Mercado
        fields = "__all__"
        
class ListaSerializer(ModelSerializer):
    class Meta:
        model = Lista
        fields = "__all__"
        
class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"