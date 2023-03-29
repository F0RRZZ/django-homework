from django.db.models import Manager, Max, Min, Count, Avg


class RatingManager(Manager):
    @staticmethod
    def queryset_sorter(queryset, sort_type):
        if sort_type == 'max':
            queryset = (
                queryset.annotate(max_rating=Max('rating'))
                .order_by('-max_rating', '-id')
                .first()
            )
        else:
            queryset = (
                queryset.annotate(min_rating=Min('rating'))
                .order_by('min_rating', '-id')
                .first()
            )

        return queryset

    def get_users_items_list(self, user_id):
        return (
            self.get_queryset()
            .select_related('item__category')
            .filter(user_id=user_id)
            .order_by('rating')
        )

    def get_users_item(self, user_id, sort_type):
        queryset = (
            self.get_queryset().filter(user_id=user_id).select_related('item')
        )
        queryset = self.queryset_sorter(queryset, sort_type)
        if queryset is not None:
            return queryset.item

    def get_users_ratings_count_and_avg(self, user_id):
        return (
            self.get_queryset()
            .filter(user_id=user_id)
            .aggregate(
                ratings_count=Count('rating'),
                ratings_avg=Avg('rating'),
            )
        )

    def get_items_ratings_count_and_avg(self, item_id):
        return (
            self.get_queryset()
            .filter(item_id=item_id)
            .aggregate(
                ratings_count=Count('rating'),
                ratings_avg=Avg('rating'),
            )
        )

    def get_item_rater(self, item_id, sort_type):
        queryset = (
            self.get_queryset().filter(item_id=item_id).select_related('user')
        )
        queryset = self.queryset_sorter(queryset, sort_type)

        if queryset is not None:
            return queryset.user
