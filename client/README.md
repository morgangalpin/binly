# binly

  Robot client!

## Prerequisites

The client project has dependencies that require **Node 4.x.x and NPM 3.x.x**.

## Installation

### Install NPM

NPM comes bundled with Node.js so [download](https://nodejs.org/download/) and install Node.js.

### Install Dependencies

```bash
cd client
npm install
npm install -g @angular/cli
```

**Trouble Installing angular-cli?**

Try:
```bash
npm install @angular/cli
```

This installs angular-cli into your client directory.
So later running an application build or serve, use the ng path instead of the global path:
 ```bash
 cd client

./node_modules/angular-cli/bin/ng build

or

./node_modules/angular-cli/bin/ng serve
```

### Set Environment Variables

 ```
"environments": {
  "dev": "src/environments/environment.ts",
  "prod": "src/environments/environment.prod.ts"
}
```

## Development server

### Serve
Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

### Build
Run `ng build`.
The build artifacts will be stored in the `static/` directory.

## Production server

### Serve

Run `ng serve --target=production --environment=prod` for a prod server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

### Build

Run `ng build --target=production --environment=prod`
The build artifacts will be stored in the `static/` directory.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive/pipe/service/class`.
Visit [Angular-CLI](https://github.com/angular/angular-cli) for more info

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).
Before running the tests make sure you are serving the app via `ng serve`.
