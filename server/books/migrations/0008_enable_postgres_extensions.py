from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('books', '0007_bookreview_downvotes_count_reviewvote'),
    ]

    operations = [
        migrations.RunSQL(
            sql='CREATE EXTENSION IF NOT EXISTS pg_trgm;',
            reverse_sql='DROP EXTENSION IF EXISTS pg_trgm;'
        ),
    ] 