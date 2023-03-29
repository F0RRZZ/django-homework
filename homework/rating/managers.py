from django.db.models import Manager, Max, Min, Count, Avg


class RatingManager(Manager):
    def get_users_best_item(self, user_id):
        return (
            self.get_queryset()
            .filter(user_id=user_id)
            .annotate(max_rating=Max('rating'))
            .order_by('-max_rating', '-id')
            .first()
            .item
        )

    def get_users_worst_item(self, user_id):
        return (
            self.get_queryset()
            .filter(user_id=user_id)
            .annotate(min_rating=Min('rating'))
            .order_by('min_rating', '-id')
            .first()
            .item
        )

    def get_users_ratings_count(self, user_id):
        return (
            self.get_queryset()
            .filter(user_id=user_id)
            .aggregate(ratings_count=Count('rating'))
        )

    def get_users_ratings_avg(self, user_id):
        return (
            self.get_queryset()
            .filter(user_id=user_id)
            .aggregate(ratings_avg=Avg('rating'))
        )

    def get_users_item_list(self, user_id):
        return self.get_queryset().filter(user_id=user_id).order_by('rating')

    def get_items_ratings_count(self, item_id):
        return (
            self.get_queryset()
            .filter(item_id=item_id)
            .aggregate(ratings_count=Count('rating'))
        )

    def get_items_ratings_avg(self, item_id):
        return (
            self.get_queryset()
            .filter(item_id=item_id)
            .aggregate(ratings_avg=Avg('rating'))
        )

    def get_item_top_rater(self, item_id):
        return (
            self.get_queryset()
            .filter(item_id=item_id)
            .annotate(max_rating=Max('rating'))
            .order_by('-max_rating', '-id')
            .first()
            .user
        )

    def get_item_bottom_rater(self, item_id):
        return (
            self.get_queryset()
            .filter(item_id=item_id)
            .annotate(min_rating=Min('rating'))
            .order_by('min_rating', '-id')
            .first()
            .user
        )
