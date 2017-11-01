import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material';

import { GpsComponent } from './gps.component';
import { GpsService } from './gps.service';

@NgModule({
  imports: [
    CommonModule,
    MatCardModule
  ],
  declarations: [GpsComponent],
  providers: [
    GpsService
  ],
  exports: [GpsComponent]
})
export class GpsModule { }
