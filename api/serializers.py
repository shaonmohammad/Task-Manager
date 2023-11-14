# serializers.py
from rest_framework import serializers
from tasks.models import Task, TaskImage


class TaskImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ('id', 'task', 'images')


class TaskSerializers(serializers.ModelSerializer):
    images = TaskImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False), write_only=True
    )

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'due_date', 'priority',
                  'is_complete', 'created_at', 'last_updated_at', 'user', 'images', 'uploaded_images')
        read_only_fields = ('user',)

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        task = Task.objects.create(**validated_data)
        for image in uploaded_images:
            task_image = TaskImage.objects.create(task=task, images=image)
        return task
