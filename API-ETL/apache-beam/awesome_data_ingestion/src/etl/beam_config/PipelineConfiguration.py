def DefaultPipeConfig():
    import apache_beam as beam
    from apache_beam.options.pipeline_options import PipelineOptions

    pipe_options = PipelineOptions()
    pipe_options.view_as(
        beam.options.pipeline_options.SetupOptions
    ).save_main_session = True

    print("Pipeline - 200 OK")

    return pipe_options
