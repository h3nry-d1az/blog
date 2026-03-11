# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

<div class="theorem">
    example theorem
</div>

<div class="proof">

Some $\LaTeX$ **here** 'n' there.

</div>

More $\LaTeX$ also **here**

```c++
#include <iostream>
#include <algorithm>
#include <cstdint>
#include <execution>

#define M 1000000007

constexpr uint8_t ns = {
#embed "numbers.bin"
};

int main()
{
    uint64_t prod = std::reduce(std::execution::par_unseq,
        ns, ns + sizeof(ns), [](const uint64_t& a, const uint64_t& b) {
            return (a * b) % M;
        });

    std::cout << prod << std::endl;
    return 0;
}
```