class Figure {
    constructor(canvas, x, y, filled) {
        this.fill = filled;
        this.startX = x;
        this.startY = y;
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');

        this.ctx.beginPath();
        this.ctx.moveTo(this.startX, this.startY);
    }

    set_fill(fill_value) {
        this.fill = fill_value;
    }

    draw() {
        throw 'Abstract method';
    }

    redraw(width, height) {
        throw 'Abstract method';
    }

    reset() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }

}