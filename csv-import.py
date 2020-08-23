import ocldev.oclresourcelist
import ocldev.oclfleximporter


csv_filename = '<csv-filename>'
ocl_env_url = '<ocl-api-endpoint>'
ocl_api_token = '<ocl-api-token>'

csv_resource_list = ocldev.oclresourcelist.OclCsvResourceList.load_from_file(csv_filename)
json_resource_list = csv_resource_list.convert_to_ocl_formatted_json()
json_resource_list.validate()

import_response = ocldev.oclfleximporter.OclBulkImporter.post(
    input_list=json_resource_list, api_url_root=ocl_env_url, api_token=ocl_api_token)
import_response.raise_for_status()
import_response_json = import_response.json()
bulk_import_task_id = import_response_json['task']

bulk_import_status_url = '%s/manage/bulkimport/?task=%s' % (ocl_env_url, bulk_import_task_id)
print 'Bulk Import Task ID: %s' % bulk_import_task_id
print 'Bulk Import Status URL: %s' % bulk_import_status_url
