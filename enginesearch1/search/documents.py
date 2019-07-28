from django_elasticsearch_dsl import DocType, Index
from account.models import Mixture

mixtures = Index('mixtures')

@mixtures.doc_type
class MixtureDocument(DocType):
	class Meta:
		model = Mixture

		fields = [
			'name',
			'slug',
			'description',
			'stock',
]