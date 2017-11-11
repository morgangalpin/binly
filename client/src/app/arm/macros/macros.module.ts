import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule, MatButtonModule } from '@angular/material';
import { FlexLayoutModule } from '@angular/flex-layout';

import { MacrosComponent } from './macros.component';

@NgModule({
  imports: [
    CommonModule,
    MatCardModule,
    MatButtonModule,
    FlexLayoutModule
  ],
  declarations: [MacrosComponent],
  exports: [MacrosComponent],
  providers: []
})
export class MacrosModule { }
