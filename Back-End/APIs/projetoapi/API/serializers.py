from rest_framework import serializers

from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
    def create(self, validated_data):
        return Usuario.objetos.create(**validated_data)
    
    def update(self, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.usuario = validated_data.get('usuario', instance.usuario)
        instance.senha = validated_data.get('senha', instance.senha)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
