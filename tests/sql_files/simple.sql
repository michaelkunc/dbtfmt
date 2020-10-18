{{
    config(
        materialized="table",
        sort = 'result_date',
        post_hook=[
            'GRANT SELECT ON {{ this }} TO GROUP ADMIN',
            'GRANT SELECT ON {{ this }} TO GROUP ANALYST',
            'GRANT SELECT ON {{ this }} TO GROUP APPLICATION',
            'GRANT SELECT ON {{ this }} TO GROUP DJANGO'
        ]
    )
}}  

SELECT
    t.column_one,
    t.column_two
  FROM
    test_table t