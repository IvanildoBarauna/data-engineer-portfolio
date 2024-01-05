import subprocess
import json
"""
Instructions for use:
    1. Download, Install and initialize Google Cloud SDK CLI >>> https://cloud.google.com/sdk/docs/install?hl=pt-br
    2. Set SDK_FOLDER in variable bin_path
"""

bin_path = "/Users/ivanildo.junior/onedrive_link/google-cloud-sdk/bin/"

def TableMetadataInfo(project: str, table_path: str):

    def TablePropertiesFromBQ():
        command = "bq show --format=prettyjson " + project + ":" + table_path 
        process = subprocess.Popen(bin_path + command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()

        return output.decode('utf-8')

    output = TablePropertiesFromBQ()
    output =  json.loads(output)
    schema =  output["schema"]

    print(" " * 40)

    print("#" * 10 + " " + table_path + " field_info " +  "#" * 10)

    for field in schema["fields"]:
        if field["name"] == 'DT_COLETA':
            lst = print("DATE_SUB(CURRENT_TIMESTAMP, INTERVAL 1 DAY) DT_COLETA,")
        else:
            print(f'{field["name"]},')
            
    print(" " * 40)

    def ClusterInfo():
        try:
            cluster_info =  output["clustering"]
            source = "cluster"
        except:
            cluster_info = output["labels"]
            source = "labels"
        
        return {
            "source": source,
            "data": cluster_info
        }
        
    print(f'{"#" * 10} {table_path} {ClusterInfo()["source"]} {"#" * 10}')

    print(ClusterInfo()["data"])
            
    print(" " * 40)

    print("#" * 10 + " " + table_path + " timePartitioning_info " +  "#" * 10)

    print(output["timePartitioning"])    
            
    print(" " * 40)

    if ClusterInfo()["source"] != "labels":
        print("#" * 10 + " " + table_path + " labels_info " +  "#" * 10)
        print(output["labels"])    
        print(" " * 40)
        

def StreamsetsPipelineInfo(project: str, dataset: str, table_name: str):
    query = f""" 
        WITH
            SS_PIPELINE AS (
            SELECT
                *
            FROM
                {project}.CONTROL.pipelines_streamsets_vw)
            SELECT
                database_schema,
                database_offset_column,
                query,
                labels
            FROM SS_PIPELINE
            WHERE
            bigquery_dataset = "{dataset}"
            and lower(database_table) = "{table_name.lower()}"
    """
    command = "bq query --format=prettyjson " + "'" + query + "'"
    process = subprocess.Popen(bin_path + command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    output = output.decode('utf-8') 
    
    print(" " * 40)
    print("#" * 10 + "streamsets pipeline information") 
    print(output)
    
    return output