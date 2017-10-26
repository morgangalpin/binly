import { Injectable } from "@angular/core";
import { Formatter } from './Formatter';
import { FormatterSet } from './FormatterSet';

@Injectable()
export class ForwardBackwardFormatterSet extends FormatterSet {

    constructor() {
        super([
            new Formatter('Backward {value}', function(values: Object) {
                let result = values['value'] && values['value'] < 0;
                if (result) {
                    values['value'] = -values['value'];
                }
                return result;
            }),
            new Formatter('Forward {value}', function(values: Object) {
                return values['value'] && values['value'] > 0;
            }),
            new Formatter('Stop', function(values: Object) {
                return values['value'] !== undefined && values['value'] == 0;
            }),
            new Formatter('Unknown')
        ]);
    }
}
