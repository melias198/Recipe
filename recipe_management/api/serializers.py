# serializers.py
from rest_framework import serializers
from .models import Recipe, Ingredient, Comment

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Recipe
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    recipe = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
