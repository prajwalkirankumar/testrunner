tuqquery.n1ql_rbac_2.RbacN1QL:
    test_select,users=ritam,roles=admin
    test_select,users=ritam,roles=views_admin
    test_select,users=ritam,roles=views_admin[default]
    test_select,default_bucket=False,sasl_buckets=1,users=ritam,roles=views_admin[bucket0]
    test_select,users=ritam,roles=query_select,all_buckets=True,force_clean=True,GROUP=P0
    test_select,users=ritam,roles=bucket_full_access[default],force_clean=True,GROUP=P0
    test_select,default_bucket=False,sasl_buckets=1,users=ritam,roles=query_select[bucket0],force_clean=True,GROUP=P0
    test_insert,users=ritam,roles=admin,force_clean=True,GROUP=P0
    test_insert,users=ritam,roles=query_insert,all_buckets=True,force_clean=True,GROUP=P0
    test_insert,users=ritam,roles=query_insert[default],force_clean=True,GROUP=P0
    test_insert,default_bucket=False,sasl_buckets=1,users=ritam,roles=query_insert[bucket0],force_clean=True,GROUP=P0
    test_update,users=ritam,roles=admin,force_clean=True,reload_data=True,GROUP=P0
    test_update,users=ritam,roles=query_update,all_buckets=True,force_clean=True,reload_data=True,GROUP=P0
    test_select,users=ritam,roles=query_select[default],force_clean=True,GROUP=P0
    test_select,users=ritam,roles=select[default],force_clean=True,GROUP=P0
    test_insert,users=ritam,roles=bucket_full_access[default],force_clean=True,GROUP=P0
    test_update,users=ritam,roles=bucket_full_access[default],force_clean=True,reload_data=True,GROUP=P0
    test_update,users=ritam,roles=query_update[default],force_clean=True,reload_data=True,GROUP=P0
    test_update,users=ritam,roles=update[default],force_clean=True,reload_data=True,GROUP=P0
    test_delete,users=ritam,roles=bucket_full_access[default)],force_clean=True,reload_data=True,GROUP=P0
    test_delete,users=ritam,roles=delete[default],force_clean=True,reload_data=True,GROUP=P0
    test_update,default_bucket=False,sasl_buckets=1,users=ritam,roles=query_update[bucket0],force_clean=True,reload_data=True,GROUP=P0
    test_delete,users=ritam,roles=admin,force_clean=True,reload_data=True,GROUP=P0
    test_delete,users=ritam,roles=query_delete,all_buckets=True,force_clean=True,reload_data=True,GROUP=P0
    test_delete,users=ritam,roles=query_delete[default],force_clean=True,reload_data=True,GROUP=P0
    test_delete,default_bucket=False,sasl_buckets=1,users=ritam,roles=query_delete[bucket0],force_clean=True,reload_data=True,GROUP=P0
    test_upsert,users=ritam,roles=admin,force_clean=True,GROUP=P0
    test_merge,users=ritam,roles=admin,force_clean=True,GROUP=P0
    test_query_select_role,users=ritam,roles=select[default],nodes_init=2,standard_buckets=1,doc-per-day=1,force_clean=True,GROUP=P0
    test_query_insert_role,users=ritam,roles=insert[default],nodes_init=2,standard_buckets=1,doc-per-day=1,force_clean=True,GROUP=P0
    test_query_update_role,users=ritam,roles=update[default],nodes_init=2,standard_buckets=1,doc-per-day=1,force_clean=True,GROUP=P0
    test_query_delete_role,users=ritam,roles=delete[default],standard_buckets=1,force_clean=True,GROUP=P0
    test_create_build_index,users=ritam,roles=admin,force_clean=True,GROUP=P0
    test_create_build_index,default_bucket=False,sasl_buckets=1,users=ritam,roles=bucket_admin[bucket0],force_clean=True,GROUP=P0
    test_create_build_index,users=ritam,roles=views_admin,all_buckets=True,force_clean=True,GROUP=P0
    test_create_build_index,users=ritam,roles=views_admin[default],force_clean=True,GROUP=P0
    test_create_build_index,default_bucket=False,sasl_buckets=1,users=ritam,roles=views_admin(bucket0),force_clean=True,GROUP=P0
    test_create_build_index,users=ritam,roles=query_manage_index,all_buckets=True,force_clean=True,GROUP=P0
    test_create_build_index,users=ritam,roles=query_manage_index[default],force_clean=True,GROUP=P0
    test_create_build_index,default_bucket=False,sasl_buckets=1,users=ritam,roles=query_manage_index(bucket0),force_clean=True,GROUP=P0
    test_upsert,users=ritam,roles=bucket_full_access[default],force_clean=True,GROUP=P0
    test_upsert,users=ritam,roles=update(default),insert(default),select[default],force_clean=True,GROUP=P0
    test_prepare,users=ritam,roles=bucket_full_access[default],force_clean=True,GROUP=P0
    test_prepare,users=ritam,roles=query_select[default],force_clean=True,GROUP=P0
    test_prepare,users=ritam,roles=select[default],force_clean=True,GROUP=P0
    test_prepare,users=ritam,roles=query_update[default],force_clean=True,GROUP=P0
    test_prepare,users=ritam,roles=update[default],force_clean=True,GROUP=P0
    test_prepare,users=ritam,roles=query_insert[default],force_clean=True,GROUP=P0
    test_prepare,users=ritam,roles=insert[default],force_clean=True,GROUP=P0
    test_prepare,users=ritam,roles=query_delete[default],force_clean=True,GROUP=P0
    test_prepare,users=ritam,roles=delete[default],force_clean=True,GROUP=P0
    test_infer,users=ritam,roles=bucket_full_access[default],force_clean=True,GROUP=P0
    test_explain,users=ritam,roles=query_select[default],force_clean=True,GROUP=P0
    test_explain,users=ritam,roles=select[default],force_clean=True,GROUP=P0
    test_explain,users=ritam,roles=query_insert[default],force_clean=True,GROUP=P0
    test_explain,users=ritam,roles=insert[default],force_clean=True,GROUP=P0
    test_explain,users=ritam,roles=query_delete[default],force_clean=True,GROUP=P0
    test_explain,users=ritam,roles=delete[default],force_clean=True,GROUP=P0
    test_explain,users=ritam,roles=query_update[default],force_clean=True,GROUP=P0
    test_explain,users=ritam,roles=update[default],force_clean=True,GROUP=P0
    test_create_build_index,users=ritam,roles=bucket_full_access[default],force_clean=True,GROUP=P0
    test_create_drop_index,users=ritam,roles=bucket_full_access[default],force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeAdmin", "name": "Jonathan Downing", "password": "password1",,roles=admin,force_clean=True,GROUP=P0
    test_grant_role,users=ritam,roles=cluster_admin,force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeClusterAdmin", "name": "Jonathan Downing", "password": "password1",,roles=bucket_full_access[default],force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeBucketAdmin", "name": "Jonathan Downing", "password": "password1",,roles=bucket_admin[default],force_clean=True,GROUP=P0
    test_grant_role,default_bucket=False,sasl_buckets=1,users="""[{"id": "johnDoebucket0", "name": "Jonathan Downing", "password": "password1",,roles=bucket_admin(bucket0),force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeViewsAdmin", "name": "Jonathan Downing", "password": "password1",,roles=views_admin,all_buckets=True,force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeViewsAdminDefault", "name": "Jonathan Downing", "password": "password1",,roles=views_admin[default],force_clean=True,GROUP=P0
    test_grant_role,default_bucket=False,sasl_buckets=1,users="""[{"id": "johnDoeViewsAdminbucket0", "name": "Jonathan Downing", "password": "password1",,roles=views_admin(bucket0),force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeManagIndex", "name": "Jonathan Downing", "password": "password1",,roles=query_manage_index,all_buckets=True,force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeManageIndexDefault", "name": "Jonathan Downing", "password": "password1",,roles=query_manage_index[default],force_clean=True,GROUP=P0
    test_grant_role,default_bucket=False,sasl_buckets=1,users="""[{"id": "johnDoeSasl", "name": "Jonathan Downing", "password": "password1",,roles=query_manage_index(bucket0),force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeSelect", "name": "Jonathan Downing", "password": "password1",,roles=select[default],force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeInsert", "name": "Jonathan Downing", "password": "password1",,roles=insert[default],force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeUpdate", "name": "Jonathan Downing", "password": "password1",,roles=update[default],force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeDelete", "name": "Jonathan Downing", "password": "password1",,roles=delete[default],force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeSys", "name": "Jonathan Downing", "password": "password1",,roles=query_system_catalog,force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeDataReader", "name": "Jonathan Downing", "password": "password1",,roles=data_reader[default],force_clean=True,GROUP=P0
    test_grant_role,default_bucket=False,sasl_buckets=1,users="""[{"id": "johnDoeWriter", "name": "Jonathan Downing", "password": "password1",,roles=data_writer(bucket0),force_clean=True,GROUP=P0
    test_grant_role,users="""[{"id": "johnDoeRepAdmin", "name": "Jonathan Downing", "password": "password1",,roles=replication_admin,force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeAdmin", "name": "Jonathan Downing", "password": "password1",,roles=admin,force_clean=True,GROUP=P0
    test_revoke_role,users=ritam,roles=cluster_admin,force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeClusterAdmin", "name": "Jonathan Downing", "password": "password1",,roles=bucket_full_access[default],force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeBucketAdmin", "name": "Jonathan Downing", "password": "password1",,roles=bucket_admin[default],force_clean=True,GROUP=P0
    test_revoke_role,default_bucket=False,sasl_buckets=1,users="""[{"id": "johnDoebucket0", "name": "Jonathan Downing", "password": "password1",,roles=bucket_admin(bucket0),force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeViewsAdmin", "name": "Jonathan Downing", "password": "password1",,roles=views_admin,all_buckets=True,force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeViewsAdminDefault", "name": "Jonathan Downing", "password": "password1",,roles=views_admin[default],force_clean=True,GROUP=P0
    test_revoke_role,default_bucket=False,sasl_buckets=1,users="""[{"id": "johnDoeViewsAdminbucket0", "name": "Jonathan Downing", "password": "password1",,roles=views_admin(bucket0),force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeManagIndex", "name": "Jonathan Downing", "password": "password1",,roles=query_manage_index,all_buckets=True,force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeManageIndexDefault", "name": "Jonathan Downing", "password": "password1",,roles=query_manage_index[default],force_clean=True,GROUP=P0
    test_revoke_role,default_bucket=False,sasl_buckets=1,users="""[{"id": "johnDoeSasl", "name": "Jonathan Downing", "password": "password1",,roles=query_manage_index(bucket0),force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeSelect", "name": "Jonathan Downing", "password": "password1",,roles=select[default],force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeInsert", "name": "Jonathan Downing", "password": "password1",,roles=insert[default],force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeUpdate", "name": "Jonathan Downing", "password": "password1",,roles=update[default],force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeDelete", "name": "Jonathan Downing", "password": "password1",,roles=delete[default],force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeSys", "name": "Jonathan Downing", "password": "password1",,roles=query_system_catalog,force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeDataReader", "name": "Jonathan Downing", "password": "password1",,roles=data_reader[default],force_clean=True,GROUP=P0
    test_revoke_role,default_bucket=False,sasl_buckets=1,users="""[{"id": "johnDoeWriter", "name": "Jonathan Downing", "password": "password1",,roles=data_writer(bucket0),force_clean=True,GROUP=P0
    test_revoke_role,users="""[{"id": "johnDoeRepAdmin", "name": "Jonathan Downing", "password": "password1",,roles=replication_admin,force_clean=True,GROUP=P0
    test_create_drop_index,users=ritam,roles=admin,force_clean=True,GROUP=P0
    test_create_drop_index,users=ritam,roles=views_admin,all_buckets=True,force_clean=True,GROUP=P0
    test_create_drop_index,users=ritam,roles=views_admin[default],force_clean=True,GROUP=P0
    test_create_drop_index,default_bucket=False,sasl_buckets=1,users=ritam,roles=views_admin(bucket0),force_clean=True,GROUP=P0
    test_create_drop_index,users=ritam,roles=query_manage_index,all_buckets=True,force_clean=True,GROUP=P0
    test_create_drop_index,users=ritam,roles=query_manage_index[default],force_clean=True,GROUP=P0
    test_create_drop_index,default_bucket=False,sasl_buckets=1,users=ritam,roles=query_manage_index(bucket0),force_clean=True,GROUP=P0
    test_prepare,users=ritam,roles=admin,force_clean=True,GROUP=P0
    test_infer,users=ritam,roles=admin,force_clean=True,GROUP=P0
    test_infer,users=ritam,roles=views_admin,all_buckets=True,force_clean=True,GROUP=P0
    test_infer,users=ritam,roles=views_admin[default],force_clean=True,GROUP=P0
    test_infer,default_bucket=False,sasl_buckets=1,users=ritam,roles=views_admin(bucket0),force_clean=True,GROUP=P0
    test_explain,users=ritam,roles=admin,force_clean=True,GROUP=P0
    test_explain,users=ritam,roles=views_admin,all_buckets=True,force_clean=True,GROUP=P0
    test_explain,users=ritam,roles=views_admin[default],force_clean=True,GROUP=P0
    test_explain,default_bucket=False,sasl_buckets=1,users=ritam,roles=views_admin(bucket0),force_clean=True,GROUP=P0
    test_create_user_roles,users=ritam,roles=admin,force_clean=True,GROUP=P0
    test_update_user_roles,users=ritam,roles=admin,new_role=cluster_admin,force_clean=True,GROUP=P0
    test_delete_user_roles,users=ritam,roles=admin,force_clean=True,GROUP=P0
    test_incorrect_n1ql_role,users=ritam,roles=query_insert[default],force_clean=True,GROUP=P0
    test_grant_incorrect_user,users=ritam,roles=admin,force_clean=True,GROUP=P0
    test_grant_incorrect_role,users=ritam,roles=admin,force_clean=True,GROUP=P0
    test_insert_nested_with_select_with_full_access,users=ritam,roles=query_insert[default],force_clean=True,GROUP=P1
    test_insert_nested_with_select_with_no_access,users=ritam,roles=query_insert[default],force_clean=True,GROUP=P1
    test_update_nested_with_select_with_full_access,users=ritam,roles=query_update[default],force_clean=True,GROUP=P1
    test_update_nested_with_select_with_no_access,users=ritam,roles=query_update[default],force_clean=True,GROUP=P1
    test_delete_nested_with_select_with_full_access,users=ritam,roles=query_delete[default],force_clean=True,GROUP=P1
    test_delete_nested_with_select_with_no_access,users=ritam,roles=query_delete[default],force_clean=True,GROUP=P1
    test_insert_nested_with_select_with_full_access_and_diff_buckets,sasl_buckets=1,users=ritam,roles=query_insert[default],force_clean=True,GROUP=P1
    test_insert_nested_with_select_with_no_access_and_diff_buckets,sasl_buckets=1,users=ritam,roles=query_insert[default],force_clean=True,GROUP=P1
    test_update_nested_with_select_with_full_access_and_diff_buckets,sasl_buckets=1,users=ritam,roles=query_update[default],force_clean=True,GROUP=P1
    test_update_nested_with_select_with_no_access_and_diff_buckets,sasl_buckets=1,users=ritam,roles=query_update[default],force_clean=True,GROUP=P1
    test_delete_nested_with_select_with_full_access_and_diff_buckets,sasl_buckets=1,users=ritam,roles=query_delete[default],force_clean=True,GROUP=P1
    test_delete_nested_with_select_with_no_access_and_diff_buckets,sasl_buckets=1,users=ritam,roles=query_delete[default],force_clean=True,GROUP=P1
    test_select_system_catalog,users=ritam,roles=admin,standard_buckets=1,doc-per-day=1,force_clean=True,GROUP=P1
    test_select_system_catalog,users=ritam,roles=views_admin[default],standard_buckets=1,force_clean=True,GROUP=P1

