class Polygon extends Figure{
    constructor(canvas, x, y, endX = [], endY = []) {
        super(canvas, x, y, true, 'Polygon');
        this.currentX = null;
        this.currentY = null;

        this.endX = endX;
        this.endY = endY;
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.moveTo(this.startX, this.startY);
        for(let i = 0; i < this.endX.length; i++) {
            this.ctx.lineTo(this.endX[i], this.endY[i]);
        }
        if(this.currentY && this.currentX)
            this.ctx.lineTo(this.currentX, this.currentY);
        this.ctx.fill();
        this.ctx.closePath();
    }

    fix() {
        if (this.currentY === null && this.currentX === null)
            return;
        this.endX.push(this.currentX);
        this.endY.push(this.currentY);
    }

    redraw(x, y) {
        this.reset();
        this.currentX = x;
        this.currentY = y;
        this.draw();
    }

    get_json() {
        let res = super.get_json();
        res['type']='Polygon';
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