import { Injectable } from "@angular/core";
import { Formatter } from './Formatter';
import { FormatterSet } from './FormatterSet';

@Injectable()
export class UpDownFormatterSet extends FormatterSet {

    constructor() {
        super([
            new Formatter('Down {value}', function(values: Object) {
                let result = values['value'] && values['value'] < 0;
                if (result) {
                    values['value'] = -values['value'];
                }
                return result;
            }),
            new Formatter('Up {value}', function(values: Object) {
                return values['value'] && values['value'] > 0;
            }),
            new Formatter('Center', function(values: Object) {
                return values['value'] !== undefined && values['value'] == 0;
            }),
            new Formatter('Unknown')
        ]);
    }
}
