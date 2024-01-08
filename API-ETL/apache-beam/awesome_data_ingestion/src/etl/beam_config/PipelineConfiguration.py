def DefaultPipeConfig():
    import apache_beam as beam
    from apache_beam.options.pipeline_options import PipelineOptions

    import logging

    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)

    try:
        pipe_options = PipelineOptions()
        pipe_options.view_as(
            beam.options.pipeline_options.SetupOptions
        ).save_main_session = True
        logging.info("Pipeline configuration DONE")
    except Exception as err:
        logging.error(f"Pipeline error configuration {err}")

    return pipe_options
