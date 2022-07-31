import sys
import timeit
from memory_profiler import profile

import server
import client



# Create memory check when execute timer
@profile(precision=6, stream=open('server_performance.log', 'w+'))
def server_performance():
    server.start_server(5050)
    # Create timer for recursive version coding with arguments graph
    t = timeit.Timer("main()",
                     setup="from __main__ import main"
                     )
    # display execution time for desired numbers of runs
    print('Elapsed time for server response: ', t.timeit(number=100))




if __name__ == "__main__":
    server_performance()
