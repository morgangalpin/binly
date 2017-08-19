
export abstract class AbstractValueLabel {
    public label: string;

    constructor(
        readonly positiveLabel: string = null,
        readonly negativeLabel: string = null,
        readonly zeroLabel: string = null
    ) {}

    // Update the label value based on the given value.
    abstract update(value);
}