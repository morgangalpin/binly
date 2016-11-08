import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { MaterialModule } from '@angular/material';

import { AppComponent } from './app.component';

// Shared module
import { SharedModule } from "./shared/shared.module";

import { CameraModule } from './camera/camera.module';
import { GpsModule } from './gps/gps.module';
import { RudderModule } from './rudder/rudder.module';
import { ThrottleModule } from './throttle/throttle.module';

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
    CameraModule,
    GpsModule,
    RudderModule,
    ThrottleModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
