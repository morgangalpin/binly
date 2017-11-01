import { Injectable } from "@angular/core";
import { Formatter } from './Formatter';
import { FormatterSet } from './FormatterSet';

@Injectable()
export class PositiveNegativeFormatterSet extends FormatterSet {

    constructor(positiveLabel: string, negativeLabel: string, zeroLabel: string) {
        super([
            new Formatter(negativeLabel + ' {value}', function(values: Object) {
                let result = values['value'] && values['value'] < 0;
                if (result) {
                    values['value'] = -values['value'];
                }
                return result;
            }),
            new Formatter(positiveLabel + ' {value}', function(values: Object) {
                return values['value'] && values['value'] > 0;
            }),
            new Formatter(zeroLabel, function(values: Object) {
                return values['value'] !== undefined && values['value'] == 0;
            }),
            new Formatter('Unknown')
        ]);
    }
}
