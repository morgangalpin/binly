import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { MaterialModule } from '@angular/material';

import { AppComponent } from './app.component';

// Shared module
import { SharedModule } from "./shared/shared.module";

import { ControlModule } from './control/control.module';
import { SpeedModule } from './speed/speed.module';
import { PositionModule } from './position/position.module';
import { CameraModule } from './camera/camera.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    MaterialModule.forRoot(),

    SharedModule,

    // Custom Modules
    ControlModule,
    SpeedModule,
    PositionModule,
    CameraModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
