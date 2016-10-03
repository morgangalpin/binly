import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MaterialModule } from '@angular/material';

import { SpeedComponent } from './speed.component';
import { SpeedService } from './speed.service';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    MaterialModule
  ],
  declarations: [SpeedComponent],
  exports: [SpeedComponent],
  providers: [SpeedService]
})
export class SpeedModule { }
