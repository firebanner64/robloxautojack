import config
import generate

if __name__ == "__main__":
    config_instance = config.Config().prompt_console_configuration()

    if config_instance.mode == 1:
        generate.jj(config_instance)
    if config_instance.mode == 2:
        generate.hj(config_instance)
    if config_instance.mode == 3:
        generate.dj(config_instance)
    if config_instance.mode == 4:
        generate.cj(config_instance)
