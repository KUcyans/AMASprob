#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iostream>
#include <memory>
#include <vector>

class RNG {
   private:
    int number;
    std::string filename;
    std::vector<double> vec;
    void generate(const int& n) {
        for (size_t i = 0; i < n; i++) {
            vec.push_back((rand() % 100) / 100.0);
        }
    }

   public:
    RNG(const int& n, const std::string& f) : number(n), filename(f) {
        generate(this->number);
    }
    ~RNG() {
        std::ofstream outFile(filename);
        if (outFile.is_open()) {
            for (size_t i = 0; i < vec.size(); ++i) {
                outFile << vec[i] << std::endl;
            }
        } else {
            std::cout << "Writing failure.\n";
        }
    }
};

int main(void) {
    srand(time(0));
    const int N = 100 * 1000;
    std::unique_ptr<RNG> obj_x = std::make_unique<RNG>(N, "randoms_x.txt");
    std::unique_ptr<RNG> obj_y = std::make_unique<RNG>(N, "randoms_y.txt");

    return 0;
}