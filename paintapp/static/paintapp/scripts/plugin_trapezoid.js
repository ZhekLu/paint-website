class TrapezoidPlugin{
    constructor(canvas, x, y, filled = false, endX=0, endY=0) {
        this.type = 'TrapezoidPlugin';
        this.fill = filled;
        this.startX = x;
        this.startY = y;
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');

        this.ctx.beginPath();
        this.ctx.moveTo(this.startX, this.startY);

        this.endX = endX;
        this.endY = endY;
    }


    set_fill(fill_value) {
        this.fill = fill_value;
    }

    set_fill_color(color) {
        this.fill_color = color;
    }

    set_stroke_color(color) {
        this.stroke_color = color;
    }

    set_width(value) {
        this.width = value;
    }

    set_params(stroke, fill, width) {
        this.set_stroke_color(stroke);
        this.set_fill_color(fill);
        this.set_width(width);
    }

    reset() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }

    is_fillable() {
        return this.fill !== null;
    }


    restore(context) {
        let fill = context.fill_color,
            stroke = context.stroke_color,
            width = context.lineWidth,
            original_ctx = this.ctx;

        context.fillStyle = this.fill_color;
        context.strokeStyle = this.stroke_color;
        context.lineWidth = this.width;
        this.ctx = context;

        this.draw();

        context.fillStyle = fill;
        context.strokeStyle = stroke;
        context.lineWidth = width;
        this.ctx = original_ctx;
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.moveTo(this.startX, this.startY - this.endY);

        let right_top_X = Math.abs(this.startX - this.endX) / 3;

        this.ctx.lineTo(right_top_X, this.startY);
        this.ctx.lineTo(2 * right_top_X, this.startY);
        this.ctx.lineTo(this.endX, this.endY);

        this.ctx.stroke();
        if(this.fill) {
            this.ctx.fill();
        }
        this.ctx.closePath();
    }

    redraw(x, y) {
        this.reset();
        this.endX = x;
        this.endY = y;
        this.draw();
    }

    get_json() {
        return {
            "type": 'PluginTrapezoid',
            "startX": this.startX,
            "startY": this.startY,
            "width": this.width,
            "stroke_color": this.stroke_color,
            "fill": this.fill,
            "fill_color": this.fill_color,
            "endX": this.endX,
            "endY": this.endY
        };
    }

    load_params_from_json(params) {
        this.startX = params.startX;
        this.startY = params.startY;
        this.width = params.width;
        this.stroke_color = params.stroke_color;
        this.fill = params.fill;
        this.fill_color = params.fill_color;
        this.endX = params.endX;
        this.endY = params.endY;
    }
}