import numpy
import enum
import typing

def normalize(
    signal: numpy.ndarray,
    new_min: typing.Optional[float] = 0.0,
    new_max: typing.Optional[float] = 1.0
) -> numpy.ndarray:
    """Normalize a signal.

    Args:
        signal (numpy.ndarray): a signal
        new_min (typing.Optional[float], optional): New min. Defaults to 0.0.
        new_max (typing.Optional[float], optional): New max. Defaults to 1.0.

    Returns:
        numpy.ndarray: normalized signal
    """
    min_ = signal.min()
    max_ = signal.max()
    return ( (signal - min_) * (new_max - new_min) / (max_ - min_) ) + new_min


#TODO : TEST

# class ConversionMethod(enum.Enum):
#     LIGHTNESS_METHOD = 0
#     AVERAGE_METHOD = 1
#     LUMINOSITY_METHOD = 2

# def lightness_method(red: numpy.ndarray, green: numpy.ndarray, blue: numpy.ndarray) -> numpy.ndarray:
#     return (numpy.min(red, green, blue) + numpy.max(red, green, blue) ) / 2

def average_method(red: numpy.ndarray, green: numpy.ndarray, blue: numpy.ndarray) -> numpy.ndarray:
    """Convert RGB image to graylevel with average method.

    Args:
        red (numpy.ndarray): red channel
        green (numpy.ndarray): green channel
        blue (numpy.ndarray): blue channel

    Returns:
        graylevel image
    """
    return (red + green + blue) / 3

def luminosity_method(red: numpy.ndarray, green: numpy.ndarray, blue: numpy.ndarray) -> numpy.ndarray:
    """Convert RGB image to graylevel with luminosity method.

    Args:
        red (numpy.ndarray): red channel
        green (numpy.ndarray): green channel
        blue (numpy.ndarray): blue channel

    Returns:
        graylevel image
    """
    return 0.299 * red + 0.587 * green + 0.114 * blue

# def from_rgb(image: numpy.ndarray, method: ConversionMethod) -> numpy.ndarray:

#     res: numpy.ndarray = None
#     red_channel, green_channel, blue_channel = image[0], image[1], image[2]

#     if method == ConversionMethod.LIGHTNESS_METHOD:
#         res = lightness_method(red_channel, green_channel, blue_channel)
#     elif method == ConversionMethod.AVERAGE_METHOD:
#         res = average_method(red_channel, green_channel, blue_channel)
#     elif method == ConversionMethod.LUMINOSITY_METHOD:
#         res = luminosity_method(red_channel, green_channel, blue_channel)

#     return res

# def nb_graylevel(grayscale_image: numpy.ndarray) -> float:
#     """Get number of graylevel in image

#     Args:
#         grayscale_image (numpy.ndarray): grayscale image

#     Returns:
#         number of graylevel
        
#     Warning:
#         - You must not apply processing on grayscale image like 
#             normalization by exemple because image's pixel must
#             be integers
#     """
#     level_min = numpy.min(grayscale_image)
#     level_max = numpy.max(grayscale_image)
#     return level_max-level_min+1

# def dynamic_graylevel(grayscale_image: numpy.ndarray) -> float:
#     level_min = numpy.min(grayscale_image)
#     level_max = numpy.max(grayscale_image)
#     return numpy.log2(level_max-level_min)


# def binarization(grayscale_image: numpy.ndarray, threshold: int, inf_sup: tuple[int, int] = (0, 1)) -> numpy.ndarray:
#     #TODO : TEST
#     res = numpy.copy(grayscale_image)
#     mask = res <= threshold
#     res[~mask] = inf_sup[0]
#     res[mask] = inf_sup[1]
    

# def binarization2(grayscale_image: numpy.ndarray, threshold: int, window_size: int, inf_sup: tuple[int, int] = (0, 1)) -> numpy.ndarray:

#     #TODO : TEST

#     res = numpy.zeros_like(grayscale_image)

#     for row in range(0, grayscale_image.shape[0]-window_size):
#         for column in range(0, grayscale_image.shape[1]-window_size):
#             current_pixel = grayscale_image[row, column]
#             average = numpy.mean(grayscale_image[row:row+window_size, column:column+window_size])
#             if(current_pixel < average-threshold):
#                 res[row, column] = inf_sup[0]
#             else:
#                 res[row, column] = inf_sup[1]

#     return res
