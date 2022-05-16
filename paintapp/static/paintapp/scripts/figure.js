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
        if (this.fill !== null)
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

    is_fillable() {
        return this.fill !== null;
    }

    get_json() {
        let figure = {
            "type":'Figure',
            "startX":this.startX,
            "startY":this.startY
        };
        if (this.is_fillable())
            figure["fill"] = this.fill;
        return figure;
    }

}