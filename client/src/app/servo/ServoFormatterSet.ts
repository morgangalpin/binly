import { Injectable } from "@angular/core";
import { FormatterSet, Formatter } from '../shared';

@Injectable()
export class ServoFormatterSet extends FormatterSet {

    constructor() {
        super([
            new Formatter('Left {value}', function(values: Object) {
                return values['value'] && values['value'] > 0;
            }),
            new Formatter('Right {value}', function(values: Object) {
                return values['value'] && values['value'] < 0;
            }),
            new Formatter('Left {value}', function(values: Object) {
                return values['value'] && values['value'] == 0;
            })
        ]);
    }
}
