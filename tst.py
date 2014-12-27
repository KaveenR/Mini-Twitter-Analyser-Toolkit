txt="""{
    "created_at": "Thu Dec 25 19:36:11 +0000 2014",
    "id": 548200551737860100,
    "id_str": "548200551737860096",
    "text": "Give a break #PresPollSL",
    "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
    "truncated": false,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "user": {
        "id": 2837780509,
        "id_str": "2837780509",
        "name": "Kaveen Rodrigo",
        "screen_name": "UKaveenR",
        "location": "Sri Lanka ",
        "url": "http://geeknirvana.org",
        "description": "Open Source Activist. Manages @SiripalaBot , Computer hobbyist proud Linux user",
        "protected": false,
        "verified": false,
        "followers_count": 186,
        "friends_count": 336,
        "listed_count": 6,
        "favourites_count": 933,
        "statuses_count": 1209,
        "created_at": "Thu Oct 02 08:26:55 +0000 2014",
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": true,
        "lang": "en",
        "contributors_enabled": false,
        "is_translator": false,
        "profile_background_color": "000000",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
        "profile_background_tile": false,
        "profile_link_color": "DD2E44",
        "profile_sidebar_border_color": "000000",
        "profile_sidebar_fill_color": "000000",
        "profile_text_color": "000000",
        "profile_use_background_image": false,
        "profile_image_url": "http://pbs.twimg.com/profile_images/543826633619013633/3axNp-Ix_normal.jpeg",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/543826633619013633/3axNp-Ix_normal.jpeg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/2837780509/1419083764",
        "default_profile": false,
        "default_profile_image": false,
        "following": null,
        "follow_request_sent": null,
        "notifications": null
    },
    "geo": {
        "type": "Point",
        "coordinates": [
            6.895782,
            79.914537
        ]
    },
    "coordinates": {
        "type": "Point",
        "coordinates": [
            79.914537,
            6.895782
        ]
    },
    "place": {
        "id": "173c2bb9d42baaa5",
        "url": "https://api.twitter.com/1.1/geo/id/173c2bb9d42baaa5.json",
        "place_type": "country",
        "name": "Sri Lanka",
        "full_name": "Sri Lanka",
        "country_code": "LK",
        "country": "Sri Lanka",
        "bounding_box": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        79.6557723320001,
                        5.92373281500009
                    ],
                    [
                        79.6557723320001,
                        9.82957591400009
                    ],
                    [
                        81.8903100920002,
                        9.82957591400009
                    ],
                    [
                        81.8903100920002,
                        5.92373281500009
                    ]
                ]
            ]
        },
        "attributes": {}
    },
    "contributors": null,
    "retweet_count": 0,
    "favorite_count": 0,
    "entities": {
        "hashtags": [
            {
                "text": "PresPollSL",
                "indices": [
                    13,
                    24
                ]
            }
        ],
        "trends": [],
        "urls": [],
        "user_mentions": [],
        "symbols": []
    },
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "filter_level": "medium",
    "lang": "en",
    "timestamp_ms": "1419536171265"
}"""
import json
a = json.loads(txt)