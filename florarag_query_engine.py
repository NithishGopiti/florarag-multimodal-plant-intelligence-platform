TOP_DISEASE_QUERY = '''
SELECT
    disease_name,
    COUNT(*) AS total_cases
FROM plant_diagnosis
GROUP BY disease_name
'''
