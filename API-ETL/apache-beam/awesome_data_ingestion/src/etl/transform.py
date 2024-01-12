from venv import create
import apache_beam as beam
import pyarrow.parquet as pq
from apache_beam.options.pipeline_options import PipelineOptions

from .logs import ConsoleInfo, WarningInfo



class ReadParquet(beam.DoFn):
    def __init__(self, ExtractedFiles: list) -> None:
        self.ExtractedFiles = ExtractedFiles    
        self.pipe_options = PipelineOptions(['--runner', 'Direct'])
    
    def process(self, element):
        parquet_file = pq.ParquetFile(element)
        
        for i in range(parquet_file.num_row_groups):
            # Lê um grupo específico
            table = parquet_file.read_row_group(i)
            # Converte cada linha em um dicionário
            for row in table:
                yield row.as_py()

def PipeRun(self):
    for file in self.ExtractedFiles:    
        with beam.Pipeline(options=self.pipe_options) as pipe:
            p =(
                pipe 
                | "CreateBeam" >> beam.Create([file])    
                | "ReadParquet" >> beam.ParDo()
            )
            
        
        
