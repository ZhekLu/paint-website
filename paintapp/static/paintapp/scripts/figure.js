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

    set_fill_color(color) {
        this.fill_color = color;
    }

    set_stroke_color(color) {
        this.stroke_color = color;
    }

    set_colors(stroke, fill) {
        this.set_stroke_color(stroke);
        this.set_fill_color(fill);
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
            "startY":this.startY,
            "stroke_color":this.stroke_color
        };
        if (this.is_fillable()) {
            figure["fill"] = this.fill;
            figure['fill_color'] = this.fill_color;
        }
        return figure;
    }

    restore() {}
}