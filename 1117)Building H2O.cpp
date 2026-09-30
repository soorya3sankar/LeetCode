class H2O {
public:

    binary_semaphore Oxy{0};

    counting_semaphore<2> Hy{2};

    atomic<int> h = 0;

    H2O() {
        
    }

    void hydrogen(function<void()> releaseHydrogen) {

        Hy.acquire();

        releaseHydrogen();

        if(++h == 2) {
            Oxy.release();
        }
    }

    void oxygen(function<void()> releaseOxygen) {

        Oxy.acquire();

        releaseOxygen();

        h = 0;

        Hy.release();
        Hy.release();
    }
};
