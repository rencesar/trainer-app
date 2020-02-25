from django.test import TestCase

from model_bakery import baker

from trainer.serializers import TrainerCreateSerializer, TrainerSerializer
from user.models import User, City


class _TrainerSerializer(TestCase):
    string_fields = (
        'slug', 'email', 'first_name', 'last_name',
        'phone_number', 'sex',
    )
    boolean_fields = ('is_active', 'is_athlete', 'is_trainer', )
    date_fields = ('birthday', )
    relation_fields = ('city', )

    def assert_fields(self, data):
        for field in self.string_fields:
            self.assertEqual(data[field], getattr(self.trainer, field))
        for field in self.boolean_fields:
            self.assertEqual(data[field], getattr(self.trainer, field))
        for field in self.date_fields:
            self.assertEqual(data[field], str(getattr(self.trainer, field)))
        for field in self.relation_fields:
            self.assertEqual(data[field], getattr(self.trainer, field).id)


class TrainerSerializerReadTestCase(_TrainerSerializer):
    string_fields = (
        'slug', 'email', 'first_name', 'last_name',
        'phone_number', 'sex',
    )
    boolean_fields = ('is_active', 'is_athlete', 'is_trainer', )
    date_fields = ('birthday', )
    relation_fields = ('city', )

    def setUp(self):
        self.trainer = baker.make(User, is_trainer=True)

    def test_all_fields_in_serializer(self):
        trainer_data = TrainerSerializer(self.trainer).data
        self.assert_fields(trainer_data)


class TrainerSerializerWriteTestCase(_TrainerSerializer):
    default_add_data = {
        'is_trainer': True,
        'is_active': False,
        'is_athlete': False
    }

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.city = baker.make(City)

    def get_dummy_data(self):
        return {
            'email': 'test@test.com',
            'first_name': 'Test',
            'last_name': 'Test',
            'birthday': '2020-02-25',
            'phone_number': 'JwKnbzqwvPwJVRe',
            'sex': 'M',
            'password': 'password123',
            'city': self.city.id
        }

    def test_success_create_trainer(self):
        data = self.get_dummy_data()
        serializer = TrainerCreateSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.trainer = instance
        data.update(**self.default_add_data)
        data['slug'] = 'testtestcom'
        self.assert_fields(data)

    def test_success_valid_data(self):
        data = self.get_dummy_data()
        serializer = TrainerCreateSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_fail_create_trainer_without_first_name(self):
        data = self.get_dummy_data()
        del data['first_name']
        serializer = TrainerCreateSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_fail_create_trainer_without_last_name(self):
        data = self.get_dummy_data()
        del data['last_name']
        serializer = TrainerCreateSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_fail_create_trainer_without_email(self):
        data = self.get_dummy_data()
        del data['email']
        serializer = TrainerCreateSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_fail_create_trainer_without_password(self):
        data = self.get_dummy_data()
        del data['password']
        serializer = TrainerCreateSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_fail_create_trainer_without_birthday(self):
        data = self.get_dummy_data()
        del data['birthday']
        serializer = TrainerCreateSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_fail_create_trainer_without_phone_number(self):
        data = self.get_dummy_data()
        del data['phone_number']
        serializer = TrainerCreateSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_fail_create_trainer_without_city(self):
        data = self.get_dummy_data()
        del data['city']
        serializer = TrainerCreateSerializer(data=data)
        self.assertFalse(serializer.is_valid())
