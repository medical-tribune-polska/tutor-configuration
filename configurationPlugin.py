from tutor import hooks
hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "FEATURES['ALLOW_PUBLIC_ACCOUNT_CREATION'] = False"
    )
)
hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "FEATURES['ENABLE_HELP_LINK'] = False"
    )
)
hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "FEATURES['ENABLE_COURSEWARE_SEARCH'] = True"
    )
)
hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "FEATURES['ENABLE_TEAMS'] = False"
    )
)
hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "FEATURES['ENABLE_ACCOUNT_DELETION'] = False"
    )
)
hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "FEATURES['SKIP_EMAIL_VALIDATION'] = True"
    )
)

# =============================================================================
# PASSWORD HASHING CONFIGURATION (bcrypt for Content Service compatibility)
# =============================================================================

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        """
# Password hashers - ORDER MATTERS!
# 1. BCryptPasswordHasher - PRIMARY for new passwords and OAuth2 authentication
# 2. PBKDF2 - Fallback for existing Open edX passwords
# 3. PreHashedBCryptPasswordHasher - LAST, only for verifying pre-hashed passwords from Content Service
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptPasswordHasher',                        # PRIMARY - new passwords
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',                        # Fallback
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',                    # Fallback
    'lms.djangoapps.custom_admin_api.hashers.PreHashedBCryptPasswordHasher',  # LAST - only for verification
]
"""
    )
)

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-cms-common-settings",
        """
# Password hashers for CMS
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptPasswordHasher',                        # PRIMARY
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',                        # Fallback
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',                    # Fallback
    'lms.djangoapps.custom_admin_api.hashers.PreHashedBCryptPasswordHasher',  # LAST
]
"""
    )
)

# Install bcrypt package in LMS container
hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-dockerfile-pre-assets",
        "RUN pip install 'bcrypt==4.0.1'"
    )
)
