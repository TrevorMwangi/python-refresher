def heavy_computation():
    import time
    time.sleep(5)

def run():
    print("Starting the computation....")
    heavy_computation()
    print("Computation complete!!")

if __name__ == "__main__":
    run()


'''
In this example, the module is imported inside the function,
so it is only loaded when the function is called.

This can help improve startup times, reduce memory usage and
avoid circular imports.
There is a possibility of dealyed errors which can make debugging 
difficult in complex code and readability can be compromised.
'''

# Using importlib to effect a lazy import


