
export class Formatter {

    constructor(
        private readonly template: string = null,
        private readonly test?: (values: Object) => boolean
    ) {}

    // Returns whether or not this formatter should be apply'd to the map of values.
    applies(values: Object): boolean {
      return !this.test || this.test(values);
    }

    // Update the label value based on the given values.
    apply(values: Object): string {
      let result = this.template;
      for (let key in values) {
        result = result.replace(new RegExp('{' + key + '}', 'g'), values[key]);
      }
      return result;
    }

}
