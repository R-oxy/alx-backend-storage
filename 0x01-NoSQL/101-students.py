#!/usr/bin/env python3
"""
Returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Return all students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]

    result = list(mongo_collection.aggregate(pipeline))

    for student in result:
        student["_id"] = str(student["_id"])

    return result
