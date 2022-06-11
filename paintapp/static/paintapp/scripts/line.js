class Line extends Figure{
    constructor(canvas, x, y, endX=0, endY=0) {
        super(canvas, x, y, null, 'Line');
        this.endX = endX;
        this.endY = endY;
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.moveTo(this.startX, this.startY);
        this.ctx.lineTo(this.endX, this.endY);
        this.ctx.stroke();
        this.ctx.closePath();
    }

    redraw(x, y) {
        this.reset();
        this.endX = x;
        this.endY = y;
        this.draw();
    }

    get_json() {
        let res = super.get_json();
        res['type']='Line';
        res['endX'] = this.endX;
        res['endY'] = this.endY;
        return res;
    }

    load_params_from_json(params) {
        super.load_params_from_json(params);
        this.endX = params.endX;
        this.endY = params.endY;
    }
}