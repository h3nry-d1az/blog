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

$$
    \sum_a^b f' = f(b) - f(a)
$$

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

Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.

Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.

Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.

Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.

Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.

[{
ctx.scale = 20

triangle = Polygon.triangle_from_lengths(13, 14, 15)
circle = Circle.triangle_incenter(
    triangle.points[0], triangle.points[1], triangle.points[2], zord=-1
)

I = (circle.x, circle.y)

ctx.add(triangle)
ctx.add(circle, fill="gray")
ctx.add(Path(triangle.points[0], I, zord=2))
ctx.add(Path(triangle.points[1], I, zord=2))
ctx.add(Path(triangle.points[2], I, zord=2))
ctx.add(Label(I[0] + 1, I[1] + 1, r"\partial \text A"), font_scale=2.5)

ctx.add(Polygon(triangle.points[0], I, triangle.points[1], zord=-2), fill="green")

print(ctx.svg())
}]

aaa