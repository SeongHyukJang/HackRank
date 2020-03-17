class Polygon
{
    constructor(arr)
    {
        this.arr = arr;
    }
    perimeter()
    {
        this.perimeter = 0;

        for(let i = 0;i<this.arr.length;i++)
        {
            this.perimeter += this.arr[i];
        }
        return this.perimeter;
    }

}

const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());