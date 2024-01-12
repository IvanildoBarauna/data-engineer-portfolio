from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam as beam

class TransformAPIData:
    def __init__(self, FolderFiles) -> None:
        self.path =  FolderFiles
        self.pipe_options = PipelineOptions([
            '--runner', 'Direct'
        ])
        
    def PipelineRun(self):
        with beam.Pipeline(options=self.pipe_options) as p:
            beam_pipe = (
                p 
                | "ReadFromParquetFile" >> beam.io.ReadFromParquetBatched(self.path)
                | "Parquet to Pandas" >> beam.Map(lambda x: x.to_pandas())
                | "Printing DataFrame" >> beam.Map(print)
            )
            