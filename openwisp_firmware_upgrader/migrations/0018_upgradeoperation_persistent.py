from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firmware_upgrader", "0017_alter_batchupgradeoperation_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="upgradeoperation",
            name="persistent",
            field=models.BooleanField(
                default=False,
                help_text=(
                    "When enabled, the operation will remain pending and "
                    "automatically retry when the device comes back online."
                ),
            ),
        ),
        migrations.AddField(
            model_name="upgradeoperation",
            name="retry_count",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Number of persistent retry attempts after initial failure.",
            ),
        ),
        migrations.AddField(
            model_name="upgradeoperation",
            name="next_retry_at",
            field=models.DateTimeField(
                blank=True,
                db_index=True,
                null=True,
                help_text="When the next periodic retry should be attempted.",
            ),
        ),
        migrations.AlterField(
            model_name="upgradeoperation",
            name="status",
            field=models.CharField(
                choices=[
                    ("in-progress", "in progress"),
                    ("success", "success"),
                    ("failed", "failed"),
                    ("cancelled", "cancelled"),
                    ("aborted", "aborted"),
                    ("pending", "pending"),
                ],
                default="in-progress",
                max_length=12,
            ),
        ),
    ]
